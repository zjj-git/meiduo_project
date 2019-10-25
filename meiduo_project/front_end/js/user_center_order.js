var vm = new Vue({
    el: '#app',
    // 修改Vue变量的读取语法，避免和django模板语法冲突
    delimiters: ['[[', ']]'],
    data: {
        host: host,
        username: sessionStorage.username || localStorage.username,
        user_id: sessionStorage.user_id || localStorage.user_id,
        token: sessionStorage.token || localStorage.token,
        orders: '', // 数据
        page: 1, // 当前页数
        page_size: 5, // 每页数量
        count: 0,  // 总数量
    },
    mounted: function () {
        this.get_orders();
    },
    methods: {
        logout() {
            sessionStorage.clear();
            localStorage.clear();
            location.href = '/login.html';
        },
        on_page: function (num) {
            if (num != this.page) {
                this.page = num;
                this.get_orders();
            }
        },
        oper_btn_click(order_id, status){
            if (status == '1') {
                // 待支付
                var url = this.host + '/orders/' + order_id + '/payment/';
                axios.get(url, {
                    headers: {
                        'Authorization': 'JWT ' + this.token
                    },
                    responseType: 'json'
                })
                    .then(response => {
                        // if (response.data.code == '0') {
                            location.href = response.data.alipay_url;
                        // } else {
                        //     console.log(response.data);
                        //     alert(response.data.errmsg);
                        // }
                    })
                    .catch(error => {
                        console.log(error.response);
                    });
            } else if (status == '4') {
                // 待评价
                location.href = '/orders/comment/?order_id=' + order_id;
            } else {
                // 其他：待收货。。。
                location.href = '/';
            }
        },

        get_orders: function(){
            url = this.host + "/orders/info/";
            axios.get(this.host + '/orders/info/', {
                headers: {
                    'Authorization': 'JWT ' + this.token
                },
                params: {
                    page: this.page,
                    page_size: this.page_size
                },
                responseType: 'json'
                })
                .then(response => {
                    this.orders = response.data;
                })
                .catch(error => {
                    console.log(error.response.data);
                })
        }
    }
});
