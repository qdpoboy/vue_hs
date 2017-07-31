<template>
  <div class="container">
    <div class="modal fade bs-example-modal-lg" id="myModal" tabindex="-1" role="dialog"
         aria-labelledby="myLargeModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true"></span>
            </button>
            <h4 class="modal-title" id="myModalLabel">组建卡组</h4>
          </div>
          <div class="modal-body">
            <ul class="list-inline text-center">
              <li>
                <router-link :to="{path:'/build?r=2'}">
                  <img @click="is_start_build(2)" src="http://cha.17173.com/hs/img/class/builder_s_2.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=3'}">
                  <img @click="is_start_build(3)" src="http://cha.17173.com/hs/img/class/builder_s_3.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=4'}">
                  <img @click="is_start_build(4)" src="http://cha.17173.com/hs/img/class/builder_s_4.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=5'}">
                  <img @click="is_start_build(5)" src="http://cha.17173.com/hs/img/class/builder_s_5.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=6'}">
                  <img @click="is_start_build(6)" src="http://cha.17173.com/hs/img/class/builder_s_6.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=7'}">
                  <img @click="is_start_build(7)" src="http://cha.17173.com/hs/img/class/builder_s_7.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=8'}">
                  <img @click="is_start_build(8)" src="http://cha.17173.com/hs/img/class/builder_s_8.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=9'}">
                  <img @click="is_start_build(9)" src="http://cha.17173.com/hs/img/class/builder_s_9.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=10'}">
                  <img @click="is_start_build(10)" src="http://cha.17173.com/hs/img/class/builder_s_10.png">
                </router-link>
              </li>
            </ul>
          </div>
          <div class="modal-footer hide">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
            <button type="button" class="btn btn-primary">选择</button>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="build_left pull-left">
        <div class="top">
          <nav aria-label="Page navigation" class="pull-left">
            <ul class="pagination">
              <li class="active" @click="toggle_tab_role($event, true)">
                <a href="javascript:;" aria-label="Previous">职业卡</a>
              </li>
              <li @click="toggle_tab_role($event, false)">
                <a href="javascript:;" aria-label="Next">中立卡</a>
              </li>
            </ul>
          </nav>
          <nav aria-label="Page navigation" class="pull-left">
            <ul class="pagination cost">
              <li @click="toggle_cost(0)" :class="{active:active_cost===0}">0</li>
              <li @click="toggle_cost(1)" :class="{active:active_cost===1}">1</li>
              <li @click="toggle_cost(2)" :class="{active:active_cost===2}">2</li>
              <li @click="toggle_cost(3)" :class="{active:active_cost===3}">3</li>
              <li @click="toggle_cost(4)" :class="{active:active_cost===4}">4</li>
              <li @click="toggle_cost(5)" :class="{active:active_cost===5}">5</li>
              <li @click="toggle_cost(6)" :class="{active:active_cost===6}">6</li>
              <li @click="toggle_cost(7)" :class="{active:active_cost===7}">7+</li>
            </ul>
          </nav>
          <nav aria-label="Page navigation" class="pull-right">
            <ul class="pagination">
              <li :class="{disabled:now_page===1}" @click="toggle_previous()">
                <a href="javascript:;" aria-label="Previous">上一页</a>
              </li>
              <li :class="{disabled:now_page===page_num}" @click="toggle_next()">
                <a href="javascript:;" aria-label="Next">下一页</a>
              </li>
            </ul>
          </nav>
        </div>
        <div class="bottom">
          <div class="row">
            <div class="col-md-12">
              <ul class="list_ul" v-if="is_show">
                <li v-for="d in card_data" @click="build_in(d.id, d.name, d.cost, d.rarity)">
                  <img class="card-thumb" v-bind:src="d.img_url">
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="build_right pull-right">
        <div class="top">
          <a class="btn btn-default" @click="new_select()">新建卡组</a> <a class="btn btn-default">{{card_team_num}}/30</a>
        </div>
        <br/>
        <div class="middle">
          <button type="button" class="btn btn-success btn-block js-copy" id="share_url_button" data-container="body"
                  data-placement="right" data-content="复制成功" data-clipboard-target="#share_url">
            点击复制分享链接
          </button>
          <span id="share_url" class="share_url">{{share_url}}&all=<template v-for="item in card_team">{{item.id}}:{{item.num}}-</template></span>
          <br/>
          <li v-for="(item, index) in cost_card_num_arr">
            <div class="middle-li-num">{{item}}</div>
            <div class="middle-li-height" v-bind:style="{height: (item * 10) + 'px'}"></div>
            <div class="middle-li-index">
              <template v-if="index == 7">
                7+
              </template>
              <template v-else>
                {{index}}
              </template>
            </div>
          </li>
        </div>
        <div class="bottom">
          <li class="card_team_li pull-left" v-for="item in card_team" @click="del_card(item.id)">
            <span class="cost">{{ item.cost }}</span>&nbsp;&nbsp;&nbsp;&nbsp;
            <span v-bind:class="item.color">{{ item.name }}</span>
            <span class="card_li_num pull-right">{{ item.num }}</span>
          </li>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
  import clipboard from '../../static/js/clipboard.min.js';

  export default {
    name: 'build',
    data: function () {
      return {
        is_show: true,
        card_color_arr: {1: '', 2: 'green', 3: 'blue', 4: 'violet', 5: 'orange'},
        active_role: 0,
        active_cost: -1,
        card_data: [],
        now_page: 1,
        page_num: 0,
        card_team_num: 0,
        card_team: [],
        cost_card_num_arr: [0, 0, 0, 0, 0, 0, 0, 0],
        share_url: ''
      }
    },
    mounted: function () {
      //js实现复制功能--开始
      var btn = document.getElementById('share_url_button');
      var clipboard_obj = new clipboard(btn);//实例化
      //复制成功执行的回调，可选
      clipboard_obj.on('success', function (e) {
        $('#share_url_button').popover('show');
        //2秒后隐藏提示
        setTimeout("$('#share_url_button').popover('destroy')", 2000);
      });
      //复制失败执行的回调，可选
      clipboard_obj.on('error', function (e) {
        console.log(e);
      });
      //js实现复制功能--结束
      $('[data-toggle="popover"]').popover();
      var r = this.$route.query.r;
      if (r > 0) {
        this.is_start_build(r);
      } else {
        this.new_select();
      }
    },
    methods: {
      new_select() {
        $('#myModal').modal({backdrop: 'static'});
      },
      is_start_build(n) {
        this.share_url = window.location.host + '/#' + this.$route.path + '?r=' + n;
        var is_form_share_data = this.$route.query.all;
        $('#myModal').modal('hide');
        if (is_form_share_data) {
          this.$http.jsonp('https://mood123.com/index1.php?m=api&a=get_share_card_list_jsonp', {
            params: {
              limit: 12,
              active_role: n,
              active_cost: -1,
              page: 1,
              share_cards: is_form_share_data
            }
          }, {
            emulateJSON: true
          }).then(function (res) {
            this.is_show = true;
            this.page_num = res.data.page_count;
            this.card_data = res.data.data;
            this.build_all(res.data.selected_cards);
          }, function (res) {
            console.error(res);
          });
        } else {
          this.active_role = n;
          this.active_cost = -1;
          this.now_page = 1;
          this.card_team_num = 0;
          this.card_team = [];
          this.cost_card_num_arr = [0, 0, 0, 0, 0, 0, 0, 0];
          this.get_data_list();
        }
      },
      get_data_list() {
        this.is_show = false;
        //http://hs_cms/index.php?m=api&a=get_card_list_jsonp
        this.$http.jsonp('https://mood123.com/index1.php?m=api&a=get_card_list_jsonp', {
          params: {
            limit: 12,
            active_role: this.active_role,
            active_cost: this.active_cost,
            page: this.now_page
          }
        }, {
          emulateJSON: true
        }).then(function (res) {
          this.is_show = true;
          this.page_num = res.data.page_count;
          this.card_data = res.data.data;
        }, function (res) {
          console.error(res);
        });
      },
      build_in(card_id, card_name, card_cost, card_rarity) {
        var vue_this = this;
        var is_in_key = -1;
        var cost_card_num_arr_key = card_cost > 7 ? 7 : card_cost;
        if (this.card_team_num >= 30) {
          alert('最多30张卡牌');
          return false;
        }
        if (this.card_team.length == 0) {
          vue_this.card_team.push({
            id: card_id,
            name: card_name,
            cost: card_cost,
            num: 1,
            color: this.card_color_arr[card_rarity]
          });
          vue_this.card_team_num++;
          vue_this.cost_card_num_arr[cost_card_num_arr_key]++;
        } else {
          $.each(this.card_team, function (i, v) {
            if (v.id == card_id) {
              is_in_key = i;
              if (v.num == 1) {
                if (card_rarity < 5) {
                  v.num++;
                  vue_this.card_team[i].num = v.num;
                  vue_this.card_team_num++;
                  vue_this.cost_card_num_arr[cost_card_num_arr_key]++;
                } else {
                  //alert('该卡牌最多1张');
                }
                return false;
              } else if (v.num == 2) {
                //alert('该卡牌最多2张');
                return false;
              }
            }
          });
          if (is_in_key == -1) {
            vue_this.card_team.push({
              id: card_id,
              name: card_name,
              cost: card_cost,
              num: 1,
              color: this.card_color_arr[card_rarity]
            });
            vue_this.card_team_num++;
            vue_this.cost_card_num_arr[cost_card_num_arr_key]++;
          }
        }
        vue_this.card_team.sort(vue_this.ascend);
      },
      build_all(selected_cards){
        var vue_this = this;
        vue_this.card_team = [];
        $.each(selected_cards, function (i, v) {
          var cost_card_num_arr_key = v.cost > 7 ? 7 : v.cost;
          vue_this.card_team.push({
            id: v.id,
            name: v.name,
            cost: v.cost,
            num: v.num,
            color: vue_this.card_color_arr[v.rarity]
          });
          vue_this.card_team_num += Number(v.num);
          vue_this.cost_card_num_arr[cost_card_num_arr_key] += Number(v.num);
        });
        vue_this.card_team.sort(vue_this.ascend);
      },
      ascend(x, y) {
        return x.cost - y.cost;
      },
      del_card(card_id) {
        var vue_this = this;
        if (vue_this.card_team_num > 0) {
          $.each(vue_this.card_team, function (i, v) {
            if (v.id == card_id) {
              var cost_card_num_arr_key = v.cost > 7 ? 7 : v.cost;
              vue_this.cost_card_num_arr[cost_card_num_arr_key]--;
              if (v.num == 1) {
                vue_this.card_team.splice(i, 1);//删除该元素
                return false;
              } else if (v.num == 2) {
                v.num--;
                vue_this.card_team[i].num = v.num;
                return false;
              }
            }
          });
          vue_this.card_team_num--;
        }
      },
      toggle_cost(i) {
        this.now_page = 1;
        if (this.active_cost == i) {//取消选中
          this.active_cost = -1;
        } else {
          this.active_cost = i;
        }
        this.get_data_list(this.$route.query.r);
      },
      toggle_tab_role(event, role) {
        this.now_page = 1;
        if (role) {
          this.active_role = this.$route.query.r;
        } else {
          this.active_role = 0;
        }
        var obj = event.currentTarget;
        $(obj).addClass('active').siblings('li').removeClass('active');
        this.get_data_list();
      },
      toggle_next() {
        if (this.now_page === this.page_num) {
          return false;
        }
        this.now_page = this.now_page + 1;
        this.get_data_list();
      },
      toggle_previous() {
        if (this.now_page == 1) {
          return false;
        }
        this.now_page = this.now_page - 1;
        this.get_data_list();
      },
    }
  }
</script>
