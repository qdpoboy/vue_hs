<template id="info">
<div class="container">
  <img v-bind:src="card_info.img_url">
  <div class="table-responsive card-info-des">
    <table class="table table-hover">
      <tbody>
        <tr>
          <td width="100px">卡牌名称</td>
          <td>{{ card_info.name }}</td>
        </tr>
        <tr>
          <td>卡牌名称</td>
          <td>123</td>
        </tr>
        <tr>
          <td>卡牌名称</td>
          <td></td>
        </tr>
        <tr>
          <td>卡牌名称</td>
          <td></td>
        </tr>
        <tr>
          <td>卡牌名称</td>
          <td></td>
        </tr>
        <tr>
          <td>卡牌名称</td>
          <td></td>
        </tr>
        <tr>
          <td>卡牌名称</td>
          <td></td>
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
