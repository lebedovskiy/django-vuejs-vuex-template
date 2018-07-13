<template lang="pug">
  .app
    .header
      router-link(to='/').logo
        img(src='./assets/logo.svg')
      router-link(to='/blog').menu__item Блог
      router-link(to='/resume').menu__item Резюме
      router-link(to='/write_me').menu__item Написать мне
    router-view
    footer Powered by Lebedoskiy, 2018
</template>

<script>
export default {
  name: 'App'
}

</script>

<style lang="stylus">
.header
  background #0067AA
  height 40px
  width 100%
  padding 1% 4%
  position fixed
  top 0
  left 0
  right 0

a
  text-decoration: none;
// ToDo make normal menu (center by vertical) on iPad

.menu__item
  font-size 1em
  margin 0 5px
  padding 5px 5px
  color black
  border inset #062DAC 2px
  border-radius 15px
  background #37D7AF
  display: inline-block
  text-align center
  white-space: nowrap;
  overflow: hidden;

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
