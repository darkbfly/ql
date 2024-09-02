

const $ = new Env("波司登小程序");
let ckName = `bosideng`;
let userCookie = checkEnv(
    ($.isNode() ? process.env[ckName] : $.getdata(ckName)) || ""
);
const notify = $.isNode() ? require("./sendNotify") : "";

!(async () => {
    console.log(
        `==================================================\n 脚本执行 - 北京时间(UTC+8): ${new Date(
            new Date().getTime() +
            new Date().getTimezoneOffset() * 60 * 1000 +
            8 * 60 * 60 * 1000
).toLocaleString()} \n==================================================`
);
    //console.log(userCookie)
    if (!userCookie?.length) return console.log(`没有找到CK哦`);
    let index = 1;
    let strSplitor = "#";

    for (let user of userCookie) {
        $.log(`\n🚀 user:【${index}】 start work\n`);
        index++
        $.token = user.split(strSplitor)[0]
        $.union_id = user.split(strSplitor)[1]
        $.ckStatus = true;
        await records()
    }

    await $.sendMsg($.logs.join("\n"));
})()
    .catch((e) => console.log(e))
    .finally(() => $.done());
function getTime() {
    // 创建Date对象
    const now = new Date();
    // 获取年、月、日、时、分、秒，并格式化为两位数
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // getMonth返回的是0-11，所以需要+1
    const day = String(now.getDate()).padStart(2, '0');
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    const timestampStr = `${year}${month}${day}${hours}${minutes}${seconds}`;
    return timestampStr
    // 调用函数并打印结果
}
function MD5(data) {
    let crypto = require('crypto')
    return crypto.createHash('md5').update(data).digest('hex')
}
async function records() {
    let time = getTime()
    let nonce = $.uuid()
    let text = `${$.union_id}${$.token}${time}${nonce}`
    let config = {
        method: 'GET',
        url: `https://gwuop.bsdits.cn/points-mall/front/member/${$.union_id}/activities/1/records`,
        headers: {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Lite Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220089 MMWEBSDK/20240404 MMWEBID/8150 MicroMessenger/8.0.49.2600(0x28003156) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
            'Accept-Encoding': 'gzip,compress,br,deflate',
            'charset': 'utf-8',
            'x-nonce': nonce,
            'x-datadog-sampling-priority': '1',
            'x-timestamp': time,
            'x-datadog-origin': 'rum',
            'bgno': 'BOSIDENG',
            'x-signature': MD5(text).toUpperCase(),
            'content-type': 'application/json',
            'x-login-type': 'MiniProgram',
            'x-access-token': $.token,
            'Referer': 'https://servicewechat.com/wx3f8f90e766e5c545/355/page-frame.html'
        }
    };

    let { data: result } = await Request(config)
    if (result.code == 200) {
        if (result.result.isSigned !== 1) {
            $.log(`未签到 ===> 签到ing`)
            await signIn()
        } else {
            $.log(`已签到 ===> 什么都不做`)
        }
        $.log(`🎉 签到信息查询成功，当前签到${result.result.signedDay}天 本次签到获得积分[${result.result.records[0].rewardPoints}]`)
    } else {
        $.log(`❌ 签到信息查询失败，原因：${result.message}`)
    }
}
async function signIn() {
    let data = JSON.stringify({});
    let time = getTime()
    let nonce = $.uuid()
    let text = `${$.union_id}${$.token}${time}${nonce}`
    let config = {
        method: 'POST',
        url: 'https://gwuop.bsdits.cn/points-mall/front/points/',
        headers: {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Lite Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220089 MMWEBSDK/20240404 MMWEBID/8150 MicroMessenger/8.0.49.2600(0x28003156) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
            'Accept-Encoding': 'gzip,compress,br,deflate',
            'charset': 'utf-8',
            'x-nonce': nonce,
            'x-datadog-sampling-priority': '1',
            'x-timestamp': time,
            'x-datadog-origin': 'rum',
            'bgno': 'BOSIDENG',
            'x-signature': MD5(text).toUpperCase(),
            'content-type': 'application/json',
            'x-login-type': 'MiniProgram',
            'x-access-token': $.token,
            'Referer': 'https://servicewechat.com/wx3f8f90e766e5c545/355/page-frame.html'
        },
        data: data
    };
    let { data: result } = await Request(config)
    if (result.code == 200) {
        $.log(result)
        $.log(`🎉 签到成功`)
    } else {
        $.log(`❌ 签到失败，原因：${result.message}`)
    }
}


function checkEnv(userCookie) {
    const envSplitor = ["&", "\n"];
    console.log(userCookie);
    let userList = userCookie
        .split(envSplitor.find((o) => userCookie.includes(o)) || "&")
        .filter((n) => n);
    console.log(`共找到${userList.length}个账号`);
    return userList;
}
// prettier-ignore
function Env(t, s) { return new (class { constructor(t, s) { this.name = t; this.logs = []; this.logSeparator = "\n"; this.startTime = new Date().getTime(); Object.assign(this, s); this.log("", `\ud83d\udd14${this.name},\u5f00\u59cb!`) } isNode() { return "undefined" != typeof module && !!module.exports } isQuanX() { return "undefined" != typeof $task } queryStr(options) { return Object.entries(options).map(([key, value]) => `${key}=${typeof value === "object" ? JSON.stringify(value) : value}`).join("&") } getURLParams(url) { const params = {}; const queryString = url.split("?")[1]; if (queryString) { const paramPairs = queryString.split("&"); paramPairs.forEach((pair) => { const [key, value] = pair.split("="); params[key] = value }) } return params } isJSONString(str) { try { return JSON.parse(str) && typeof JSON.parse(str) === "object" } catch (e) { return false } } isJson(obj) { var isjson = typeof obj == "object" && Object.prototype.toString.call(obj).toLowerCase() == "[object object]" && !obj.length; return isjson } async sendMsg(message) { if (!message) return; if (this.isNode()) { await notify.sendNotify(this.name, message) } else { this.msg(this.name, "", message) } } randomNumber(length) { const characters = "0123456789"; return Array.from({ length }, () => characters[Math.floor(Math.random() * characters.length)]).join("") } randomString(length) { const characters = "abcdefghijklmnopqrstuvwxyz0123456789"; return Array.from({ length }, () => characters[Math.floor(Math.random() * characters.length)]).join("") } uuid() { return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) { var r = (Math.random() * 16) | 0, v = c == "x" ? r : (r & 0x3) | 0x8; return v.toString(16) }) } time(t) { let s = { "M+": new Date().getMonth() + 1, "d+": new Date().getDate(), "H+": new Date().getHours(), "m+": new Date().getMinutes(), "s+": new Date().getSeconds(), "q+": Math.floor((new Date().getMonth() + 3) / 3), S: new Date().getMilliseconds(), }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (new Date().getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in s) { new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? s[e] : ("00" + s[e]).substr(("" + s[e]).length))) } return t } msg(title = t, subtitle = "", body = "", options) { const formatOptions = (options) => { if (!options) { return options } else if (typeof options === "string") { if (this.isQuanX()) { return { "open-url": options } } else { return undefined } } else if (typeof options === "object" && (options["open-url"] || options["media-url"])) { if (this.isQuanX()) { return options } else { return undefined } } else { return undefined } }; if (!this.isMute) { if (this.isQuanX()) { $notify(title, subtitle, body, formatOptions(options)) } } let logs = ["", "==============📣系统通知📣=============="]; logs.push(title); subtitle ? logs.push(subtitle) : ""; body ? logs.push(body) : ""; console.log(logs.join("\n")); this.logs = this.logs.concat(logs) } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, s) { const e = !this.isQuanX(); e ? this.log("", `\u2757\ufe0f${this.name},\u9519\u8bef!`, t.stack) : this.log("", `\u2757\ufe0f${this.name},\u9519\u8bef!`, t) } wait(t) { return new Promise((s) => setTimeout(s, t)) } done(t = {}) { const s = new Date().getTime(), e = (s - this.startTime) / 1e3; this.log("", `\ud83d\udd14${this.name},\u7ed3\u675f!\ud83d\udd5b ${e}\u79d2`); this.log(); if (this.isNode()) { process.exit(1) } if (this.isQuanX()) { $done(t) } } })(t, s) }

async function Request(options) {
    if ($.isNode()) {
        const axios = require("axios");
        Request = async (options) => {
            try {
                return await axios.request(options);
            } catch (error) {
                return error && error.error ? error.error : "请求失败";
            }
        };
    }
    if ($.isQuanX()) {
        Request = async (options) => {
            try {
                return await $task.fetch(options);
            } catch (error) {
                return error && error.error ? error.error : "请求失败";
            }
        };
    }
    return await Request(options);
}