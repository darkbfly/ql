#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
签到脚本通用工具集合。

抽象常用的凭证解析、请求构造与日志/异常处理，以降低每个脚本的重复代码量并提升健壮性。
"""
import logging
import time
from typing import Any, Dict, List, Optional, Sequence, Tuple

import requests

_LOGGER = logging.getLogger("script_utils")


def _bool_from_value(value: Any) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value == 1
    if isinstance(value, str):
        lowered = value.lower()
        if lowered in {"true", "1", "success", "ok"}:
            return True
        if lowered in {"false", "0"}:
            return False
    return None


def parse_token_fields(
    raw_token: str,
    expected_fields: int,
    delimiter: str = "#",
    field_names: Optional[Sequence[str]] = None,
) -> Tuple[str, ...]:
    """
    将形如 "value1#value2#value3" 的 token 字符串拆分，并做缺失校验。

    Args:
        raw_token: 原始 token 字符串。
        expected_fields: 期望的字段数量。
        delimiter: 分隔符，默认 "#"
        field_names: 可选的字段名称列表，仅用于错误提示。

    Returns:
        Tuple[str, ...]: 拆分后的字段。

    Raises:
        ValueError: 当字段数量不足时抛出，附带可读性强的提示。
    """
    parts: List[str] = raw_token.split(delimiter)
    if len(parts) < expected_fields:
        readable_name = ", ".join(field_names) if field_names else ""
        raise ValueError(
            f"凭证格式错误，至少需要 {expected_fields} 个字段({readable_name})，实际仅 {len(parts)} 个。"
        )
    return tuple(part.strip() for part in parts[:expected_fields])


def build_weapp_headers(
    host: str,
    referer: str,
    user_agent: str,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Dict[str, str]:
    """
    构造常用的微信小程序请求头，并允许覆盖/扩展字段。
    """
    headers = {
        "Host": host,
        "Connection": "keep-alive",
        "xweb_xhr": "1",
        "User-Agent": user_agent,
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": referer,
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    if extra_headers:
        headers.update(extra_headers)
    return headers


def request_with_retry(
    session: requests.Session,
    method: str,
    url: str,
    *,
    retries: int = 2,
    backoff: float = 1.0,
    **kwargs,
) -> requests.Response:
    """
    统一的请求发送逻辑，附带重试与日志。
    """
    last_exc: Optional[Exception] = None
    for attempt in range(1, retries + 2):
        try:
            resp = session.request(method, url, timeout=10, **kwargs)
            resp.raise_for_status()
            return resp
        except Exception as exc:  # noqa: BLE001
            last_exc = exc
            _LOGGER.warning(
                "request_with_retry失败",
                extra={
                    "url": url,
                    "attempt": attempt,
                    "retries": retries,
                    "error": str(exc),
                },
            )
            if attempt > retries:
                raise
            time.sleep(backoff * attempt)
    if last_exc:
        raise last_exc
    raise RuntimeError("request_json_with_retry 未捕捉到异常但也未返回结果")


def log_event(event: str, **fields) -> None:
    """
    简易结构化日志，便于在青龙日志中快速检索关键字段。
    """
    serialized_fields = " ".join(f"{k}={v}" for k, v in fields.items())
    print(f"[{event}] {serialized_fields}")


def request_json_with_retry(
    session: requests.Session,
    method: str,
    url: str,
    *,
    retries: int = 2,
    backoff: float = 1.0,
    **kwargs,
) -> Any:
    """
    在 request_with_retry 基础上进一步解析 JSON。
    """
    resp = request_with_retry(
        session,
        method,
        url,
        retries=retries,
        backoff=backoff,
        **kwargs,
    )
    return resp.json()


def parse_response_content(resp: requests.Response) -> Any:
    """
    将响应转换为 JSON 或回退到文本，避免脚本重复处理。
    """
    try:
        return resp.json()
    except ValueError:
        return resp.text


def normalize_result(payload: Any) -> Tuple[bool, str]:
    """
    根据响应内容推断成功与否并生成可读信息。
    """
    success = False
    message = ""
    if isinstance(payload, dict):
        for key in ("success", "isSuccess", "result"):
            if key in payload:
                bool_value = _bool_from_value(payload[key])
                if bool_value is not None:
                    success = bool_value
                    break
        if not success:
            for key in ("code", "status", "errcode"):
                if key in payload:
                    code_val = str(payload[key]).upper()
                    if code_val in {"0", "200", "SUCCESS"}:
                        success = True
                    break
        message = (
            payload.get("msg")
            or payload.get("message")
            or payload.get("tips")
            or payload.get("toast")
            or payload.get("errmsg")
            or str(payload)
        )
    else:
        text = str(payload)
        success = "成功" in text and "失败" not in text
        message = text.strip() or text
    return success, message

