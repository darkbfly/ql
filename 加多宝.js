/*
微信小程序 点亮城市｜与加多宝一起喝彩

脚本兼容: QuantumultX, Surge, Loon, JSBox, Node.js
============Quantumultx===============
[task_local]
#点亮城市｜与加多宝一起喝彩
00 00 5,6,7 * * * , tag=点亮城市｜与加多宝一起喝彩, img-url=, enabled=true

================Loon==============
[Script]
cron "00 00 5,6,7 * * *" script-path=,tag=点亮城市｜与加多宝一起喝彩

===============Surge=================
点亮城市｜与加多宝一起喝彩 = type=cron,cronexp="00 00 5,6,7 * * *",wake-system=1,timeout=33600,script-path=

============小火箭=========
点亮城市｜与加多宝一起喝彩 = type=cron,script-path=, cronexpr="00 00 5,6,7 * * *", timeout=33600, enable=true
*/

const $ = new Env('点亮城市｜与加多宝一起喝彩');
$.log(`需要新建环境变量: Dlcsyjdbyqhc_token\n填写抓包token\n多用户可以用"#" "@" "\\n" 隔开`);

var appUrlArr = [];
var token = '';

!(async () => {
    //检查环境变量
    $.log(`开始检测环境变量`);
    if (!(await checkEnv())) {
        return;
    } else {
        //获取用户信息
        await initAccountInfo();
    }
})().catch((e) => $.logErr(e)).finally(() => $.done());

async function checkEnv() {
    const Dlcsyjdbyqhc_token = ($.isNode() ? (process.env.Dlcsyjdbyqhc_token) : ($.getval('Dlcsyjdbyqhc_token'))) || "";
    if (!Dlcsyjdbyqhc_token) {
        let str = Dlcsyjdbyqhc_token ? "" : "Dlcsyjdbyqhc_token";
        $.log(`未找到环境变量: ${str}\n`);
        return false;
    }
    if (Dlcsyjdbyqhc_token.indexOf('#') != -1) {
        appUrlArrs = Dlcsyjdbyqhc_token.split('#');
        $.log(`您选择的是用"#"隔开Dlcsyjdbyqhc_token\n`);
    } else if (Dlcsyjdbyqhc_token.indexOf('\n') != -1) {
        appUrlArrs = Dlcsyjdbyqhc_token.split('\n');
        $.log(`您选择的是用"\\n"隔开Dlcsyjdbyqhc_token\n`);
    } else if (Dlcsyjdbyqhc_token.indexOf('@') != -1) {
        appUrlArrs = Dlcsyjdbyqhc_token.split('@');
        $.log(`您选择的是用"@"隔开Dlcsyjdbyqhc_token\n`);
    } else {
        appUrlArrs = [Dlcsyjdbyqhc_token];
    }
    Object.keys(appUrlArrs).forEach((item) => {
        if (appUrlArrs[item]) {
            appUrlArr.push(appUrlArrs[item]);
        }
    });
    totalUser = appUrlArr.length;
    $.log(`共找到${totalUser}个用户`);
    return true;
}

async function getEnvParam(userNum) {
    let appUrlArrVal = appUrlArr[userNum];
    token = appUrlArrVal;
}

async function initAccountInfo() {
    for (numUser = 0; numUser < totalUser; numUser++) {
        $.log(`\n用户` + (numUser + 1) + `开始执行`);
        await getEnvParam(numUser);
        for (let k in appUrlArr) {
            let save_token = appUrlArr[k];
            if (save_token != `${token}`) {
                for (let m = 0; m < 2; m++) {
                    for (let l = 1; l < 5; l++) {
                        await save(save_token, l);
                        await $.wait(5000); //等待5秒
                    }
                }
            }
        }
        await drop();
        await $.wait(5000); //等待5秒
        for (let i = 1; i < 4; i++) {
            let game_name = "";
            i == 1 ? game_name = "麻辣消消乐" : i == 2 ? game_name = "极限冲击" : i == 3 ? game_name = "我要去杭州" : "";
            for (let j = 0; j < 5; j++) {
                $.log(`${game_name} 第${(j+1)}次 开始`);
                await game(i);
                await $.wait(5000); //等待5秒
                $.log(`${game_name} 第${(j+1)}次 结束`);
            }
        }
        await accumulate();
    }
}

function object2str(t) {
    var a = [];
    for (var b in t) a.push(b + "=" + t[b]);
    return a.join("&");
}

function object2query3(t) {
    var a = [];
    for (var b in t) a.push(b);
    a.sort();
    var c = [];
    for (var d in a) c.push(a[d] + "=" + t[a[d]]);
    return c.join("");
}

//助力
async function save(save_token, save_category) {
    let temporary = (new Date).getTime() + "";
    return new Promise((resolve) => {
        let url = {
            url: `https://wb.onlineweixin.com/jdbcms/assistance/save`,
            body: JSON.stringify({
                "token": `${save_token}`,
                "category": `${save_category}`,
                "temporary": `${temporary}`
            }),
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "token": `${token}`
            }
        };
        $.post(url, async (err, resp, data) => {
            try {
                if (err) {
                    $.log(`助力Api请求失败`);
                } else {
                    let html = JSON.parse(data);
                    if (html.code == 2000) {
                        $.log(`助力 ` + html.desc);
                    } else {
                        $.log(`助力 ` + html.desc);
                    }
                }
            } catch (e) {
                $.logErr(e, resp);
            } finally {
                resolve();
            }
        });
    });
}

//查询点亮值
async function accumulate() {
    return new Promise((resolve) => {
        let url = {
            url: `https://wb.onlineweixin.com/jdbcms/user/accumulate`,
            headers: {
                "token": `${token}`
            }
        };
        $.get(url, async (err, resp, data) => {
            try {
                if (err) {
                    $.log(`查询点亮值Api请求失败`);
                } else {
                    let html = JSON.parse(data);
                    if (html.code == 2000) {
                        let total = html.data.total;
                        $.log(`查询点亮值 剩余${total}`);
                    } else {
                        $.log(`查询点亮值 ` + html.desc);
                    }
                }
            } catch (e) {
                $.logErr(e, resp);
            } finally {
                resolve();
            }
        });
    });
}

//点亮城市
async function drop() {
    return new Promise((resolve) => {
        let url = {
            url: `https://wb.onlineweixin.com/jdbcms/record/drop`,
            body: JSON.stringify({
                "city": "重庆市",
                "province": "重庆市"
            }),
            headers: {
                "Content-Type": "application/json;charset=UTF-8",
                "token": `${token}`
            }
        };
        $.post(url, async (err, resp, data) => {
            try {
                if (err) {
                    $.log(`点亮城市Api请求失败`);
                } else {
                    let html = JSON.parse(data);
                    if (html.code == 2000) {
                        let integralB = html.data.integralB;
                        $.log(`点亮城市 获得${integralB}点亮值`);
                        await $.wait(5000); //等待5秒
                        await drop();
                    } else {
                        $.log(`点亮城市 ` + html.desc);
                    }
                }
            } catch (e) {
                $.logErr(e, resp);
            } finally {
                resolve();
            }
        });
    });
}

//开始游戏
async function game(game_state) {
    return new Promise((resolve) => {
        let url = {
            url: `https://wb.onlineweixin.com/jdbcms/record/game`,
            body: JSON.stringify({
                "token": `${token}`,
                "state": `${game_state}`
            }),
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            }
        };
        $.post(url, async (err, resp, data) => {
            try {
                if (err) {
                    $.log(`开始游戏Api请求失败`);
                } else {
                    let html = JSON.parse(data);
                    if (html.code == 2000) {
                        let count = html.data.count;
                        if (count > 0) {
                            $.log(`还有${count}次 游戏次数`);
                            await $.wait(90000); //等待90秒
                            await effect(`${game_state}`);
                        } else {
                            $.log(`游戏次数不足`);
                        }
                    } else {
                        $.log(`开始游戏 ` + html.desc);
                    }
                }
            } catch (e) {
                $.logErr(e, resp);
            } finally {
                resolve();
            }
        });
    });
}

async function getScore(token, gameScore, game_state) {
    let GameData = {
        token: token,
        gameScore: gameScore,
        gameStall: 0
    };
    if (game_state == 1) {
        0 <= GameData.gameScore && GameData.gameScore <= 70 ? GameData.gameStall = 1 : 70 < GameData.gameScore && GameData.gameScore <= 130 ? GameData.gameStall = 2 : 130 < GameData.gameScore && GameData.gameScore <= 180 ? GameData.gameStall = 3 : 180 < GameData.gameScore && (GameData.gameStall = 4);
        let e = (new Date).getTime() + "",
            t = Math.ceil(9 * Math.random()),
            n = e.substring(0, t) + GameData.gameStall + e.substring(t, e.length) + t,
            a = (new Date).getTime() + "",
            o = Math.ceil(9 * Math.random()),
            r = a.substring(0, o) + 2 + a.substring(o, a.length) + o,
            i = {
                storey: n,
                classification: r,
                token: GameData.token,
                Score: GameData.gameScore
            };
        return i;
    } else if (game_state == 2) {
        0 <= GameData.gameScore && GameData.gameScore <= 800 ? GameData.gameStall = 1 : 800 < GameData.gameScore && GameData.gameScore <= 1e3 ? GameData.gameStall = 2 : 1e3 < GameData.gameScore && GameData.gameScore <= 1500 ? GameData.gameStall = 3 : 1500 < GameData.gameScore && (GameData.gameStall = 4);
        let e = (new Date).getTime() + "",
            t = Math.ceil(9 * Math.random()),
            n = e.substring(0, t) + GameData.gameStall + e.substring(t, e.length) + t,
            r = (new Date).getTime() + "",
            a = Math.ceil(9 * Math.random()),
            o = r.substring(0, a) + 3 + r.substring(a, r.length) + a,
            i = {
                storey: n,
                classification: o,
                token: GameData.token,
                Score: GameData.gameScore
            };
        return i;
    } else if (game_state == 3) {
        0 <= GameData.gameScore && GameData.gameScore <= 1e4 ? GameData.gameStall = 1 : 1e4 < GameData.gameScore && GameData.gameScore <= 15e3 ? GameData.gameStall = 2 : 15e3 < GameData.gameScore && GameData.gameScore <= 2e4 ? GameData.gameStall = 3 : 2e4 < GameData.gameScore && (GameData.gameStall = 4);
        let e = (new Date).getTime() + "",
            t = Math.ceil(9 * Math.random()),
            n = e.substring(0, t) + GameData.gameStall + e.substring(t, e.length) + t,
            a = (new Date).getTime() + "",
            r = Math.ceil(9 * Math.random()),
            i = a.substring(0, r) + 4 + a.substring(r, a.length) + r,
            o = {
                storey: n,
                classification: i,
                token: GameData.token,
                Score: GameData.gameScore
            };
        return o;
    }
    return null;
}

//随机数
async function getrandom(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

//结束游戏
async function effect(game_state) {
    let gameScore = 183;
    if (game_state == 1) {
        gameScore = await getrandom(183, 210);
    } else if (game_state == 2) {
        gameScore = await getrandom(1503, 1530);
    } else if (game_state == 3) {
        gameScore = await getrandom(20003, 20030);
    }
    let effect_body = await getScore(`${token}`, gameScore, game_state);
    return new Promise((resolve) => {
        let url = {
            url: `https://wb.onlineweixin.com/jdbcms/record/effect`,
            body: JSON.stringify(effect_body),
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            }
        };
        $.post(url, async (err, resp, data) => {
            try {
                if (err) {
                    $.log(`结束游戏Api请求失败`);
                } else {
                    let html = JSON.parse(data);
                    if (html.code == 2000) {
                        let integralB = html.data.integralB;
                        $.log(`结束游戏 获得${integralB}点亮值`);
                    } else {
                        $.log(`结束游戏 ` + html.desc);
                    }
                }
            } catch (e) {
                $.logErr(e, resp);
            } finally {
                resolve();
            }
        });
    });
}

function Env(t, e) {
    class s {
        constructor(t) {
            this.env = t;
        }
        send(t, e = "GET") {
            t = "string" == typeof t ? {
                url: t
            } : t;
            let s = this.get;
            return "POST" === e && (s = this.post), new Promise((e, i) => {
                s.call(this, t, (t, s, r) => {
                    t ? i(t) : e(s);
                });
            });
        }
        get(t) {
            return this.send.call(this.env, t);
        }
        post(t) {
            return this.send.call(this.env, t, "POST");
        }
    }
    return new class {
        constructor(t, e) {
            this.name = t, this.http = new s(this), this.data = null, this.dataFile = "box.dat", this.logs = [], this.isMute = !1, this.isNeedRewrite = !1, this.logSeparator = "\n", this.startTime = (new Date).getTime(), Object.assign(this, e), this.log("", `\ud83d\udd14${this.name}, \u5f00\u59cb!`);
        }
        isNode() {
            return "undefined" != typeof module && !!module.exports;
        }
        isQuanX() {
            return "undefined" != typeof $task;
        }
        isSurge() {
            return "undefined" != typeof $httpClient && "undefined" == typeof $loon;
        }
        isLoon() {
            return "undefined" != typeof $loon;
        }
        toObj(t, e = null) {
            try {
                return JSON.parse(t);
            } catch {
                return e;
            }
        }
        toStr(t, e = null) {
            try {
                return JSON.stringify(t);
            } catch {
                return e;
            }
        }
        getjson(t, e) {
            let s = e;
            const i = this.getdata(t);
            if (i) try {
                s = JSON.parse(this.getdata(t));
            } catch {}
            return s;
        }
        setjson(t, e) {
            try {
                return this.setdata(JSON.stringify(t), e);
            } catch {
                return !1;
            }
        }
        getScript(t) {
            return new Promise(e => {
                this.get({
                    url: t
                }, (t, s, i) => e(i));
            });
        }
        runScript(t, e) {
            return new Promise(s => {
                let i = this.getdata("@chavy_boxjs_userCfgs.httpapi");
                i = i ? i.replace(/\n/g, "").trim() : i;
                let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout");
                r = r ? 1 * r : 20, r = e && e.timeout ? e.timeout : r;
                const [o, h] = i.split("@"), a = {
                    url: `http://${h}/v1/scripting/evaluate`,
                    body: {
                        script_text: t,
                        mock_type: "cron",
                        timeout: r
                    },
                    headers: {
                        "X-Key": o,
                        Accept: "*/*"
                    }
                };
                this.post(a, (t, e, i) => s(i));
            }).catch(t => this.logErr(t));
        }
        loaddata() {
            if (!this.isNode()) return {}; {
                this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path");
                const t = this.path.resolve(this.dataFile),
                    e = this.path.resolve(process.cwd(), this.dataFile),
                    s = this.fs.existsSync(t),
                    i = !s && this.fs.existsSync(e);
                if (!s && !i) return {}; {
                    const i = s ? t : e;
                    try {
                        return JSON.parse(this.fs.readFileSync(i));
                    } catch (t) {
                        return {};
                    }
                }
            }
        }
        writedata() {
            if (this.isNode()) {
                this.fs = this.fs ? this.fs : require("fs"), this.path = this.path ? this.path : require("path");
                const t = this.path.resolve(this.dataFile),
                    e = this.path.resolve(process.cwd(), this.dataFile),
                    s = this.fs.existsSync(t),
                    i = !s && this.fs.existsSync(e),
                    r = JSON.stringify(this.data);
                s ? this.fs.writeFileSync(t, r) : i ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r);
            }
        }
        lodash_get(t, e, s) {
            const i = e.replace(/\[(\d+)\]/g, ".$1").split(".");
            let r = t;
            for (const t of i)
                if (r = Object(r)[t], void 0 === r) return s;
            return r;
        }
        lodash_set(t, e, s) {
            return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), e.slice(0, -1).reduce((t, s, i) => Object(t[s]) === t[s] ? t[s] : t[s] = Math.abs(e[i + 1]) >> 0 == +e[i + 1] ? [] : {}, t)[e[e.length - 1]] = s, t);
        }
        getdata(t) {
            let e = this.getval(t);
            if (/^@/.test(t)) {
                const [, s, i] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : "";
                if (r) try {
                    const t = JSON.parse(r);
                    e = t ? this.lodash_get(t, i, "") : e;
                } catch (t) {
                    e = "";
                }
            }
            return e;
        }
        setdata(t, e) {
            let s = !1;
            if (/^@/.test(e)) {
                const [, i, r] = /^@(.*?)\.(.*?)$/.exec(e), o = this.getval(i), h = i ? "null" === o ? null : o || "{}" : "{}";
                try {
                    const e = JSON.parse(h);
                    this.lodash_set(e, r, t), s = this.setval(JSON.stringify(e), i);
                } catch (e) {
                    const o = {};
                    this.lodash_set(o, r, t), s = this.setval(JSON.stringify(o), i);
                }
            } else s = this.setval(t, e);
            return s;
        }
        getval(t) {
            return this.isSurge() || this.isLoon() ? $persistentStore.read(t) : this.isQuanX() ? $prefs.valueForKey(t) : this.isNode() ? (this.data = this.loaddata(), this.data[t]) : this.data && this.data[t] || null;
        }
        setval(t, e) {
            return this.isSurge() || this.isLoon() ? $persistentStore.write(t, e) : this.isQuanX() ? $prefs.setValueForKey(t, e) : this.isNode() ? (this.data = this.loaddata(), this.data[e] = t, this.writedata(), !0) : this.data && this.data[e] || null;
        }
        initGotEnv(t) {
            this.got = this.got ? this.got : require("got"), this.cktough = this.cktough ? this.cktough : require("tough-cookie"), this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar, t && (t.headers = t.headers ? t.headers : {}, void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar));
        }
        get(t, e = (() => {})) {
            t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"]), this.isSurge() || this.isLoon() ? (this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, {
                "X-Surge-Skip-Scripting": !1
            })), $httpClient.get(t, (t, s, i) => {
                !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i);
            })) : this.isQuanX() ? (this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, {
                hints: !1
            })), $task.fetch(t).then(t => {
                const {
                    statusCode: s,
                    statusCode: i,
                    headers: r,
                    body: o
                } = t;
                e(null, {
                    status: s,
                    statusCode: i,
                    headers: r,
                    body: o
                }, o);
            }, t => e(t))) : this.isNode() && (this.initGotEnv(t), this.got(t).on("redirect", (t, e) => {
                try {
                    if (t.headers["set-cookie"]) {
                        const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString();
                        this.ckjar.setCookieSync(s, null), e.cookieJar = this.ckjar;
                    }
                } catch (t) {
                    this.logErr(t);
                }
            }).then(t => {
                const {
                    statusCode: s,
                    statusCode: i,
                    headers: r,
                    body: o
                } = t;
                e(null, {
                    status: s,
                    statusCode: i,
                    headers: r,
                    body: o
                }, o);
            }, t => {
                const {
                    message: s,
                    response: i
                } = t;
                e(s, i, i && i.body);
            }));
        }
        post(t, e = (() => {})) {
            if (t.body && t.headers && !t.headers["Content-Type"] && (t.headers["Content-Type"] = "application/x-www-form-urlencoded"), t.headers && delete t.headers["Content-Length"], this.isSurge() || this.isLoon()) this.isSurge() && this.isNeedRewrite && (t.headers = t.headers || {}, Object.assign(t.headers, {
                "X-Surge-Skip-Scripting": !1
            })), $httpClient.post(t, (t, s, i) => {
                !t && s && (s.body = i, s.statusCode = s.status), e(t, s, i);
            });
            else if (this.isQuanX()) t.method = "POST", this.isNeedRewrite && (t.opts = t.opts || {}, Object.assign(t.opts, {
                hints: !1
            })), $task.fetch(t).then(t => {
                const {
                    statusCode: s,
                    statusCode: i,
                    headers: r,
                    body: o
                } = t;
                e(null, {
                    status: s,
                    statusCode: i,
                    headers: r,
                    body: o
                }, o);
            }, t => e(t));
            else if (this.isNode()) {
                this.initGotEnv(t);
                const {
                    url: s,
                    ...i
                } = t;
                this.got.post(s, i).then(t => {
                    const {
                        statusCode: s,
                        statusCode: i,
                        headers: r,
                        body: o
                    } = t;
                    e(null, {
                        status: s,
                        statusCode: i,
                        headers: r,
                        body: o
                    }, o);
                }, t => {
                    const {
                        message: s,
                        response: i
                    } = t;
                    e(s, i, i && i.body);
                });
            }
        }
        time(t) {
            let e = {
                "M+": (new Date).getMonth() + 1,
                "d+": (new Date).getDate(),
                "H+": (new Date).getHours(),
                "m+": (new Date).getMinutes(),
                "s+": (new Date).getSeconds(),
                "q+": Math.floor(((new Date).getMonth() + 3) / 3),
                S: (new Date).getMilliseconds()
            };
            /(y+)/.test(t) && (t = t.replace(RegExp.$1, ((new Date).getFullYear() + "").substr(4 - RegExp.$1.length)));
            for (let s in e) new RegExp("(" + s + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? e[s] : ("00" + e[s]).substr(("" + e[s]).length)));
            return t;
        }
        msg(e = t, s = "", i = "", r) {
            const o = t => {
                if (!t) return t;
                if ("string" == typeof t) return this.isLoon() ? t : this.isQuanX() ? {
                    "open-url": t
                } : this.isSurge() ? {
                    url: t
                } : void 0;
                if ("object" == typeof t) {
                    if (this.isLoon()) {
                        let e = t.openUrl || t.url || t["open-url"],
                            s = t.mediaUrl || t["media-url"];
                        return {
                            openUrl: e,
                            mediaUrl: s
                        };
                    }
                    if (this.isQuanX()) {
                        let e = t["open-url"] || t.url || t.openUrl,
                            s = t["media-url"] || t.mediaUrl;
                        return {
                            "open-url": e,
                            "media-url": s
                        };
                    }
                    if (this.isSurge()) {
                        let e = t.url || t.openUrl || t["open-url"];
                        return {
                            url: e
                        };
                    }
                }
            };
            this.isMute || (this.isSurge() || this.isLoon() ? $notification.post(e, s, i, o(r)) : this.isQuanX() && $notify(e, s, i, o(r)));
            let h = ["", "==============\ud83d\udce3\u7cfb\u7edf\u901a\u77e5\ud83d\udce3=============="];
            h.push(e), s && h.push(s), i && h.push(i), console.log(h.join("\n")), this.logs = this.logs.concat(h);
        }
        log(...t) {
            t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator));
        }
        logErr(t, e) {
            const s = !this.isSurge() && !this.isQuanX() && !this.isLoon();
            s ? this.log("", `\u2757\ufe0f${this.name}, \u9519\u8bef!`, t.stack) : this.log("", `\u2757\ufe0f${this.name}, \u9519\u8bef!`, t);
        }
        wait(t) {
            return new Promise(e => setTimeout(e, t));
        }
        done(t = {}) {
            const e = (new Date).getTime(),
                s = (e - this.startTime) / 1e3;
            this.log("", `\ud83d\udd14${this.name}, \u7ed3\u675f! \ud83d\udd5b ${s} \u79d2`), this.log(), (this.isSurge() || this.isQuanX() || this.isLoon()) && $done(t);
        }
    }(t, e);
}