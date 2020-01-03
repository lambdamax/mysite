$(function () {
    if ("WebSocket" in window) {
        var protocol = location.protocol == 'http:' ? 'ws://' : 'wss://',
            old = {}, ws;
        ConnectWs();
    }

    function ConnectWs() {
        ws = new WebSocket(protocol + window.location.host + "/wb");
        WsOptions();
    }

    function WsOptions() {
        ws.onopen = function () {
            ws.send("ws open");
        };

        ws.onmessage = function (evt) {
            var received_msg = evt.data;
            if (received_msg == 'Connection Limited') return ws.close();
            var datas = JSON.parse(received_msg);
            var info = '<table><tr>\n' +
                '<th width="35%">名称</th>\n' +
                '<th width="30%">现价</th>\n' +
                '<th width="25%">涨跌</th>\n' +
                '<th width="10%">涨幅</th>\n' +
                '</tr>';
            $.each(datas, function (i, e) {
                if (e.hasOwnProperty('rate') && e.rate) {
                    if (e.rate < 0) e.color = '#008000';
                    else {
                        e.color = '#ff0000';
                        e.rate = '+' + e.rate;
                    }
                    e.rate = e.rate + '%'
                }
                if (old[e.name] < e.price) e.flag = 'class="valup"';
                else if (old[e.name] > e.price) e.flag = 'class="valdown"';
                info += '<tr>';
                info += '<td><span>{name}</span></th>';
                info += '<td><span style="color:{color}" {flag}>{price}</span></td>';
                info += '<td><span style="color:{color}" {flag}>{range}</span></td>';
                info += '<td><span style="color:{color}" {flag}>{rate}</span></td>';
                info += '</tr>';
                info = info.format(e);
                old[e.name] = e.price;
                old.time = e.time;
            });
            info = '<p style="font-size: 10px;color: gray;width: 100%;text-align: center;">更新时间：{time}</p>'.format(old) + info + '</table>';

            $('#notice').html(info);
            setTimeout(function () {
                $('#notice span').removeClass()
            }, 1000);
        };

        ws.onclose = function () {
            ConnectWs();
        };

        ws.onerror = function (e) {
            console.log(e);
        };
    }
});
