<template lang="pug">
  .app
    .header
      router-link(to='/').logo L
      router-link(to='/blog', v-bind:class="{ mobile: isMobile }").menu__item Блог
      router-link(to='/resume', v-bind:class="{ mobile: isMobile }").menu__item Резюме
      router-link(to='/write_me', v-bind:class="{ mobile: isMobile }").menu__item Написать мне
    router-view
    footer Powered by Lebedoskiy, 2018
</template>

<script>
export default {
  name: 'App',
  computed: {
    isMobile: () => {
      let isMobile
      if (/Android|webOS|iPhone|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
        isMobile = true
      }
      return isMobile
    }
  }
}

</script>

<style lang="stylus">
.header
  background #0067AA
  height 60px
  width 90%
  margin 5px
  padding 1% 4%
  border-radius 20px

a
  text-decoration: none;
.logo
  margin 7px 0
  height 50px
  width 50px
  font-size 2.5em
  color black

.menu__item
  font-size 1.5em
  margin 10px
  padding 10px 5px
  color black
  border outset #062DAC 2px
  border-radius 15px
  background #37D7AF

.mobile
  font-size 1em
  padding: 5px

.app
  font-family: 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing: antialiased
  -moz-osx-font-smoothing: grayscale
  color: #2c3e50

footer
  height 1em
  width 100%
  padding 5px 0
  text-align center
  background #0067AA
  color white
  position fixed
  bottom 0
  left 0
  right 0
</style>
