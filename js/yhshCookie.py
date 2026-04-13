import os
import re

ENV_FILES = ['/ql/data/config/env.sh', '/ql/config/env.sh']
OUTPUT_FILE = '/ql/data/scripts/darkbfly_ql/js/pupuCookie.txt'
YHSH_OUTPUT_FILE = '/ql/data/scripts/darkbfly_ql/js/yhshCookie.txt'


def parse_env_values(env_name: str):
    def format_values(raw_value: str):
        parts = [x.strip() for x in raw_value.split('&') if x.strip()]
        return [f'{item}#' for item in parts]

    env_value = os.getenv(env_name)
    if env_value:
        return format_values(env_value)

    pattern = re.compile(
        rf'^\s*(?:export\s+)?{re.escape(env_name)}\s*=\s*(.*?)\s*$'
    )
    for env_file in ENV_FILES:
        if not os.path.isfile(env_file):
            continue
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                match = pattern.match(line)
                if not match:
                    continue
                raw_value = match.group(1).strip()
                if (
                    len(raw_value) >= 2
                    and raw_value[0] in ("'", '"')
                    and raw_value[-1] == raw_value[0]
                ):
                    raw_value = raw_value[1:-1]
                return format_values(raw_value)
    return []


if __name__ == '__main__':
    yhsh = parse_env_values('yhsh_cookies')
    pupu = parse_env_values('pupu_cookies')

    os.makedirs(os.path.dirname(YHSH_OUTPUT_FILE), exist_ok=True)
    with open(YHSH_OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(yhsh))

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(pupu))


