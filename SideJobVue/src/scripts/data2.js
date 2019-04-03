export default {
  name: 'listView1',
  data () {
    return {
      items: [],
      img_src: 'http://www.urbanbrush.net/web/wp-content/uploads/edd/2018/02/web-20180211134119206041.png'
    }
  },
  created () {
    this.$axios.get('http://soorokim.duckdns.org:19223/api/getRecruitList')
      .then((response) => {
        console.log(response.data + 'HELLLP')
        this.items = response.data
      })
  }
}
