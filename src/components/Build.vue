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
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_2.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=3'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_3.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=4'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_4.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=5'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_5.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=6'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_6.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=7'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_7.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=8'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_8.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=9'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_9.png">
                </router-link>
              </li>
              <li>
                <router-link :to="{path:'/build?r=10'}">
                  <img @click="is_start_build" src="http://cha.17173.com/hs/img/class/builder_s_10.png">
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
          <div>
            <button class="btn btn-default" type="submit">职业卡</button>
            <button class="btn btn-default" type="submit">中立卡</button>
            1 2 3 4 5 6 7+
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
        </div>
        <div class="top"></div>
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

    }
  },
  mounted: function() {
    var r = this.$route.query.r;
    if(r > 0){
      //$('#myModal').modal('hide');
    }else{
      $('#myModal').modal({backdrop: 'static'});
    }
  },
  methods:{
    is_start_build() {
      $('#myModal').modal('hide');
    }
  }
}
</script>
