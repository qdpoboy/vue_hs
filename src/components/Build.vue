<template>
  <div class="container">
    <div class="modal fade bs-example-modal-lg" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true"></span></button>
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
          <div class="modal-footer">
            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
            <button type="button" class="btn btn-primary">选择</button>
          </div>
        </div>
      </div>
    </div>
    <div>
      <div class="build_left">
        <div class="top">
          <nav aria-label="Page navigation" class="pull-left">
            <ul class="pagination">
              <li @click="toggle_tab_zhiye()">
                <a href="javascript:;" aria-label="Previous">职业卡</a>
              </li>
              <li @click="toggle_tab_zhongli()">
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
                <li v-for="d in card_data" @click="build_in(d.id)">
                  <img class="card-thumb" v-bind:src="d.img_url">
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="build_right">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'build',
  data: function() {
    return {
      is_show : true,
      active_role : 0,
      active_cost : -1,
      card_data : [],
      now_page : 1,
      page_num : 0
    }
  },
  mounted: function() {
    var r = this.$route.query.r;
    if(r > 0){
      //$('#myModal').modal('hide');
      this.is_start_build(r);
    }else{
      $('#myModal').modal({backdrop: 'static'});
    }
  },
  methods:{
    is_start_build(n) {
      $('#myModal').modal('hide');
      this.active_role = n;
      this.get_data_list();
    },
    get_data_list() {
      this.is_show = false;
      //http://hs_cms/index.php?m=api&a=get_card_list_jsonp
      this.$http.jsonp('https://mood123.com/index1.php?m=api&a=get_card_list_jsonp', {
        params:{
          limit : 12,
          active_role: this.active_role,
          active_cost: this.active_cost,
          page: this.now_page
        }
      }, {
        emulateJSON: true
      }).then(function(res) {
        this.is_show = true;
        this.page_num = res.data.page_count;
        this.card_data = res.data.data;
      }, function(res) {
        console.error(res);
      });
    },
    build_in(card_id) {
      console.log(card_id);
    },
    toggle_cost(i) {
      this.now_page = 1;
      if(this.active_cost == i){//取消选中
        this.active_cost = -1;
      }else{
        this.active_cost = i;
      }
      this.get_data_list(this.$route.query.r);
    },
    toggle_tab_zhiye() {
      this.now_page = 1;
      this.active_role = this.$route.query.r;
      this.get_data_list();
    },
    toggle_tab_zhongli() {
      this.now_page = 1;
      this.active_role = 0;
      this.get_data_list();
    }
  }
}
</script>
