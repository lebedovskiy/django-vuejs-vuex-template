<template lang="pug">
  .app
    .header
      router-link(to='/').logo
        img(src='./assets/logo.svg')
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
  height 50px
  width 100%
  padding 1% 4%
  margin 0
  position fixed
  top 0
  left 0
  right 0
  text-align left

a
  text-decoration: none;

img
  float inherit

.logo
  margin 0 0
  height 80px
  width 80px

.menu__item
  font-size 1em
  margin 10px
  padding 1% 5px
  color black
  border inset #062DAC 2px
  border-radius 15px
  background #37D7AF
  top 40px

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
