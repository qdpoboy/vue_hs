<template id="info">
<div class="container">
  <img v-bind:src="card_info.img_url">
  <div class="table-responsive card-info-des">
    <table class="table table-hover">
      <tbody>
        <tr>
          <td width="80px">卡牌名称</td>
          <td>{{ card_info.name }}</td>
        </tr>
        <tr>
          <td>简介</td>
          <td></td>
        </tr>
        <tr>
          <td>评语</td>
          <td></td>
        </tr>
        <tr>
          <td>职业</td>
          <td>{{ card_info.career_name }}</td>
        </tr>
        <tr>
          <td>稀有度</td>
          <td>{{ card_info.rarity_name }}</td>
        </tr>
        <tr>
          <td>来源</td>
          <td>{{ card_info.card_set_name }}</td>
        </tr>
        <tr>
          <td>类型</td>
          <td>{{ card_info.card_type_name }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
</template>

<script>
export default {
  name: 'info',
  data: function() {
    return {
      card_info : []
    }
  },
  mounted: function(){
    this.get_info();
  },
  methods: {
    get_info(){
      //http://hs_cms/index.php?m=api&a=get_card_info_jsonp
      this.$http.jsonp('http://mood123.com/index1.php?m=api&a=get_card_info_jsonp', {
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
