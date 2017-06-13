<template id="list">
<div class="container">
  <img src="">
</div>
</template>

<script>
export default {
  name: 'info',
  data: function() {
    return {
      card_info : {"id":"1","name":"u4f3au673au5f85u53d1","career":"7","card_set":"3","card_type":"5","cost":"0","atk":"0","health":"0","rarity":"4","windfury":"0","taunt":"0","freeze":"0","battlecry":"0","stealth":"0","combo":"0","charge":"0","grant_charge":"0","spellpower":"0","silence":"0","enrage":"0","divine_shield":"0","deathrattle":"0","secret":"0","mission":"0","img_url":"http://i1.17173cdn.com/8hpoty/YWxqaGBf/images/resource/new_middler/EX1_145.png?version=201612021432","card_url":"http://cha.17173.com/hs/info/card_zhcn/20"}
    }
  },
  mounted: function(){
    this.get_info();
  },
  methods: {
    get_info(){
      this.$http.jsonp('http://hs_cms/index.php?m=api&a=get_card_info_jsonp', {
        params:{
          id: this.$route.params.id
        }
      }, {
        emulateJSON: true
      }).then(function(res) {
        this.card_info = res.data;
      }, function(res) {
        console.error(res);
      });
    },
  }
}
</script>
