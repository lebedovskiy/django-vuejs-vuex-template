<template lang="pug">
  .main
    .presentation
      h2.presentation__text {{presentation.title}}
      .presentation__img
        img(width='100%' src='../assets/main__img.jpg')
      h3.presentation__subtitle {{presentation.subtitle}}
      p.main__text {{presentation.text}}
</template>

<script>
import {HTTP} from '../api/common'

export default {
  name: 'Main',
  data () {
    return {
      presentation: []
    }
  },
  mounted () {
    HTTP
      .get('main')
      .then(response => (this.presentation = response.data[0]))
  }
}
</script>

<style lang="stylus">
  .main
    width 60%
    height 100%
    margin 0 auto
    @media screen and (max-width: 996px)
      width 95%

  .presentation
    margin 1%
    overflow auto

  .presentation__text
    @media screen and (orientation: landscape)
      float left
      margin 1%
      width 48%

  .presentation__subtitle
    @media screen and (orientation: landscape)
      float left
      margin 1%
      width 48%

  .presentation__img
    @media screen and (orientation: landscape)
      float right
      margin 1%
      width 48%

  .main__text
    @media screen and (orientation: landscape)
      margin 1%
      width 44%
</style>
