<template lang="pug">
  .main
    .presentation
      h2.presentation__text {{presentation.title}}
      .presentation__img
        img(width='100%' src='../assets/1530346884.jpg')
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
      .get('posts')
      .then(response => (this.presentation = response.data[0]))
  }
}
</script>

<style lang="stylus">
  .main
    font-family Bahnschrift
    color #000000
    text-align center
    width 60%
    margin 0 auto
    @media screen and (max-width: 996px)
      width 100%

  .presentation
    margin 1%
    overflow auto

  .presentation__text
    text-align left
    @media screen and (max-width: 996px) and (orientation: portrait)
      color #000000
      font-family Bahnschrift
      font-size 100%
      width 95%
      padding 1%
      margin 1%
    @media screen and (orientation: landscape)
      color #000000
      float left
      font-family Bahnschrift
      font-size 150%
      margin 1%
      width 43%

  .presentation__img
    @media screen and (max-width: 996px)
      width 95%
      padding 1%
      margin 1%
    @media screen and (orientation: landscape)
      float right
      margin 1%
      width 48%

  .main__text
    line-height: 1.5
    margin 2%
    padding 0 1%
    text-align left
    width 95%
</style>
