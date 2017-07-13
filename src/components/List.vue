<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>英雄</b></li>
            <li @click="toggle_role(tab.i, tab.t)" v-for="tab in tabs_role" :class="{active:active_role===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>卡牌集</b></li>
            <li @click="toggle_ji(tab.i, tab.t)" v-for="tab in tabs_ji" :class="{active:active_ji===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>法力</b></li>
            <li @click="toggle_cost(tab.i, tab.t)" v-for="tab in tabs_cost" :class="{active:active_cost===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>类型</b></li>
            <li @click="toggle_type(tab.i, tab.t)" v-for="tab in tabs_type" :class="{active:active_type===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>种族</b></li>
            <li @click="toggle_race(tab.i, tab.t)" v-for="tab in tabs_race" :class="{active:active_race===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>等级</b></li>
            <li @click="toggle_rarity(tab.i, tab.t)" v-for="tab in tabs_rarity" :class="{active:active_rarity===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>特性</b></li>
            <li @click="toggle_feat(tab.i, tab.t)" v-for="tab in tabs_feat" :class="{active:active_feat===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>攻击</b></li>
            <li @click="toggle_atk(tab.i, tab.t)" v-for="tab in tabs_atk" :class="{active:active_atk===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li><b>生命</b></li>
            <li @click="toggle_health(tab.i, tab.t)" v-for="tab in tabs_health" :class="{active:active_health===tab.i}">
              {{tab.t}}
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <ul class="list_ul">
            <li v-for="d in card_data" v-if="is_show">
              <router-link :to="{path:'/card/'+d.id}">
                <img class="card-thumb" v-bind:src="d.img_url">
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="container">
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
</template>

<script>
export default {
  name: 'list',
  data: function() {
    return {
      is_show : true,
      card_data: [],
      page_num: 0,
      now_page: 1,
      active_role: -1,
      active_ji: -1,
      active_cost: -1,
      active_type: -1,
      active_race: -1,
      active_rarity: -1,
      active_feat: -1,
      active_atk: -1,
      active_health: -1,
      tabs_role: [{i:0,t:'中立'},{i:2,t:'德鲁伊'},{i:3,t:'猎人'},{i:4,t:'法师'},{i:5,t:'圣骑'},{i:6,t:'牧师'},{i:7,t:'潜行者'},{i:8,t:'萨满'},{i:9,t:'术士'},{i:10,t:'战士'}],
      tabs_ji: [{i:2,t:'基本级'},{i:3,t:'专家级'},{i:101,t:'纳克萨玛斯'},{i:102,t:'地精大战侏儒'},{i:103,t:'黑石山的火焰'},{i:104,t:'冠军的试炼'},{i:105,t:'探险者协会'},{i:106,t:'上古之神的低语'},{i:107,t:'卡拉赞之夜'},{i:108,t:'龙争虎斗加基森'},{i:109,t:'勇闯安哥洛'}],
      tabs_cost: [{i:0,t:'0'},{i:1,t:'1'},{i:2,t:'2'},{i:3,t:'3'},{i:4,t:'4'},{i:5,t:'5'},{i:6,t:'6'},{i:7,t:'7+'}],
      tabs_type: [{i:4,t:'随从'},{i:5,t:'法术'},{i:7,t:'武器'}],
      tabs_race: [{i:14,t:'鱼人'},{i:15,t:'恶魔'},{i:20,t:'野兽'},{i:21,t:'图腾'},{i:23,t:'海盗'},{i:24,t:'龙'},{i:25,t:'机械'},{i:26,t:'元素'}],
      tabs_rarity: [{i:1,t:'普通'},{i:2,t:'免费'},{i:3,t:'稀有'},{i:4,t:'史诗'},{i:5,t:'传说'}],
      tabs_feat: [{i:1,t:'嘲讽',e:'taunt'},{i:2,t:'冻结',e:'freeze'},{i:3,t:'风怒',e:'windfury'},{i:4,t:'战吼',e:'battlecry'},{i:5,t:'潜行',e:'stealth'},{i:6,t:'连击',e:'combo'},{i:7,t:'冲锋',e:'charge'},{i:8,t:'过载',e:'grant_charge'},{i:9,t:'法术伤害',e:'spellpower'},{i:10,t:'沉默',e:'silence'},{i:11,t:'激怒',e:'enrage'},{i:12,t:'圣盾',e:'divine_shield'},{i:13,t:'亡语',e:'deathrattle'},{i:14,t:'奥秘',e:'secret'},{i:15,t:'任务',e:'mission'}],
      tabs_atk: [{i:0,t:'0'},{i:1,t:'1'},{i:2,t:'2'},{i:3,t:'3'},{i:4,t:'4'},{i:5,t:'5'},{i:6,t:'6'},{i:7,t:'7+'}],
      tabs_health: [{i:0,t:'0'},{i:1,t:'1'},{i:2,t:'2'},{i:3,t:'3'},{i:4,t:'4'},{i:5,t:'5'},{i:6,t:'6'},{i:7,t:'7+'}]
    }
  },
  mounted: function() {
    this.get_data_list();
  },
  methods: {

    get_data_list() {
      this.is_show = false;
      //http://hs_cms/index.php?m=api&a=get_card_list_jsonp
      this.$http.jsonp('https://mood123.com/index1.php?m=api&a=get_card_list_jsonp', {
        params:{
          active_role: this.active_role,
          active_ji: this.active_ji,
          active_cost: this.active_cost,
          active_type: this.active_type,
          active_race: this.active_race,
          active_rarity: this.active_rarity,
          active_feat: this.active_feat,
          active_atk: this.active_atk,
          active_health: this.active_health,
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
    toggle_role(i, v) {
      this.now_page = 1;
      if(this.active_role == i){//取消选中
        this.active_role = -1;
      }else{
        this.active_role = i;
      }
      this.get_data_list();
    },
    toggle_ji(i, v) {
      this.now_page = 1;
      if(this.active_ji == i){//取消选中
        this.active_ji = -1;
      }else{
        this.active_ji = i;
      }
      this.get_data_list();
    },
    toggle_cost(i, v) {
      this.now_page = 1;
      if(this.active_cost == i){//取消选中
        this.active_cost = -1;
      }else{
        this.active_cost = i;
      }
      this.get_data_list();
    },
    toggle_type(i, v) {
      this.now_page = 1;
      if(this.active_type == i){//取消选中
        this.active_type = -1;
      }else{
        this.active_type = i;
      }
      this.get_data_list();
    },
    toggle_race(i, v) {
      this.now_page = 1;
      if(this.active_race == i){//取消选中
        this.active_race = -1;
      }else{
        this.active_race = i;
      }
      this.get_data_list();
    },
    toggle_rarity(i, v) {
      this.now_page = 1;
      if(this.active_rarity == i){//取消选中
        this.active_rarity = -1;
      }else{
        this.active_rarity = i;
      }
      this.get_data_list();
    },
    toggle_feat(i, v) {
      this.now_page = 1;
      if(this.active_feat == i){//取消选中
        this.active_feat = -1;
      }else{
        this.active_feat = i;
      }
      this.get_data_list();
    },
    toggle_atk(i, v) {
      this.now_page = 1;
      if(this.active_atk == i){//取消选中
        this.active_atk = -1;
      }else{
        this.active_atk = i;
      }
      this.get_data_list();
    },
    toggle_health(i, v) {
      this.now_page = 1;
      if(this.active_health == i){//取消选中
        this.active_health = -1;
      }else{
        this.active_health = i;
      }
      this.get_data_list();
    },
    toggle_next(){
      if(this.now_page === this.page_num){
        return false;
      }
      this.now_page = this.now_page + 1;
      this.get_data_list();
    },
    toggle_previous(){
      if(this.now_page == 1){
        return false;
      }
      this.now_page = this.now_page - 1;
      this.get_data_list();
    },
  }
}
</script>
