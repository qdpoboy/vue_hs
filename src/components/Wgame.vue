<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <div class="wgame-l-t">
            账号：张三<br>
            EXP：1000<br>
            LV：1<br>
            HP：100<br>
            MP：100<br>
            金钱：100<br>
            攻击力：10~20<br>
          </div>
          <div class="wgame-l-m">
            怪物：红色的小松鼠<br>
            HP：100<br>
            攻击力：10~20<br>
          </div>
          <div class="wgame-l-b">
            [12:12:12]你对小松鼠造成了11点伤害。<br>
            [12:12:12]你对小松鼠造成了11点伤害。<br>
            [12:12:12]你对小松鼠造成了11点伤害。<br>
            [12:12:12]你对小松鼠造成了11点伤害。<br>
            [12:12:12]你对小松鼠造成了11点伤害。<br>
          </div>
        </div>
        <div class="col-md-6">
          <div class="wgame-r-t">
            设置<br>
            背包<br>
            技能<br>
            <span @click="tijiao()">提交socket</span>
          </div>
          <div class="wgame-r-b">
            当前地图：新手村<br>
            史诗掉落率：9%<br>
            传说掉落率：0.1%<br>
          </div>
        </div>
      </div>
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
      tabs_ji: [{i:2,t:'基本级'},{i:3,t:'专家级'},{i:101,t:'纳克萨玛斯'},{i:102,t:'地精大战侏儒'},{i:103,t:'黑石山的火焰'},{i:104,t:'冠军的试炼'},{i:105,t:'探险者协会'},{i:106,t:'上古之神的低语'},{i:107,t:'卡拉赞之夜'},{i:108,t:'龙争虎斗加基森'},{i:109,t:'勇闯安哥洛'},{i:110,t:'冰封王座的骑士'}],
      tabs_cost: [{i:0,t:'0'},{i:1,t:'1'},{i:2,t:'2'},{i:3,t:'3'},{i:4,t:'4'},{i:5,t:'5'},{i:6,t:'6'},{i:7,t:'7+'}],
      tabs_type: [{i:4,t:'随从'},{i:5,t:'法术'},{i:7,t:'武器'},{i:8,t:'英雄'}],
      tabs_race: [{i:14,t:'鱼人'},{i:15,t:'恶魔'},{i:20,t:'野兽'},{i:21,t:'图腾'},{i:23,t:'海盗'},{i:24,t:'龙'},{i:25,t:'机械'},{i:26,t:'元素'}],
      tabs_rarity: [{i:1,t:'普通'},{i:2,t:'免费'},{i:3,t:'稀有'},{i:4,t:'史诗'},{i:5,t:'传说'}],
      tabs_feat: [{i:1,t:'嘲讽',e:'taunt'},{i:2,t:'冻结',e:'freeze'},{i:3,t:'风怒',e:'windfury'},{i:4,t:'战吼',e:'battlecry'},{i:5,t:'潜行',e:'stealth'},{i:6,t:'连击',e:'combo'},{i:7,t:'冲锋',e:'charge'},{i:8,t:'过载',e:'grant_charge'},{i:9,t:'法术伤害',e:'spellpower'},{i:10,t:'沉默',e:'silence'},{i:11,t:'激怒',e:'enrage'},{i:12,t:'圣盾',e:'divine_shield'},{i:13,t:'亡语',e:'deathrattle'},{i:14,t:'奥秘',e:'secret'},{i:15,t:'任务',e:'mission'},{i:16,t:'吸血',e:'lifesteal'}],
      tabs_atk: [{i:0,t:'0'},{i:1,t:'1'},{i:2,t:'2'},{i:3,t:'3'},{i:4,t:'4'},{i:5,t:'5'},{i:6,t:'6'},{i:7,t:'7+'}],
      tabs_health: [{i:0,t:'0'},{i:1,t:'1'},{i:2,t:'2'},{i:3,t:'3'},{i:4,t:'4'},{i:5,t:'5'},{i:6,t:'6'},{i:7,t:'7+'}]
    }
  },
  sockets:{
    connect: function(){
      this.id=this.$socket.id;
      console.log('socket connected');
    },
    customEmit: function(val){
      console.log('this method was fired by the socket server. eg: io.emit("customEmit", data)')
    },
    receiveGroupMsg(val){
      console.log('接收到的消息为' + val);
    }
  },
  mounted: function() {
    this.tijiao();
  },
  methods: {

    tijiao(){
      console.log(this.id);
      this.$socket.emit('sendGroupMsg', '11111');
    },
  }
}
</script>
