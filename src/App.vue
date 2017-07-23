<template>
  <div>
    <nav class="navbar navbar-default">
      <div class="container-fluid container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                  data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">vue版炉石卡牌模拟器</a>
        </div>
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
            <li @click="change_active(0)">
              <router-link to="/card">{{ tab1 }}</router-link>
            </li>
            <li @click="change_active(1)">
              <router-link to="/build">{{ tab2 }}</router-link>
            </li>
            <li @click="change_active(2)">
              <router-link to="/tab3">{{ tab3 }}</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
  export default {
    name: 'app',
    data: function () {
      return {
        tab1: '卡牌',
        tab2: '组卡',
        tab3: '卡组',
      }
    },
    mounted: function () {
      if (this.$route.path == '/' || this.$route.path == '/card') {
        this.change_active(0);
      } else if (this.$route.path == '/build') {
        this.change_active(1);
      }
    },
    methods: {
      change_active(obj) {
        $('.nav').find('li').eq(obj).attr('class', 'active');
        $('.nav').find('li').eq(obj).siblings().attr('class', '');
      },
    }
  }
</script>

<style>
  #app {
    color: #2c3e50;
  }
</style>
