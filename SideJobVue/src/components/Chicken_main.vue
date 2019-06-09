<template>
	<div id="app" style="text-align: center;">
		<div class="container" v-for="i in items" :key="i.id">
			<div class="item-container">
				<div class="item-header">
					<img src="@/assets/css/sample.png" width="300" height="200" />
				</div>
				<div class="item-body">
					<div class="item-title"> 
						{{i.title}}
					</div>
					<div class="item-content">
						<div style="text-align: center; height: 28px">
							{{i.view}} <br> VIEW
						</div>
						<div class="item-content-detail">
							{{i.content}}	
						</div>
						<div class="item-btn-wrap">
							<button @click="viewCount(i.recr_id)" class="item-btn">Detail</button>
						</div>
					</div>
				</div>
			</div>	
		</div>
	</div>
</template>

<script>
import { eventBus } from '../main';

export default {
  name: 'chickenMain',
  data: function () {
    return {
      items: [],
      img_src: 'http://www.urbanbrush.net/web/wp-content/uploads/edd/2018/02/web-20180211134119206041.png'
    }
  },
  created () {
    this.$axios.get('http://soorokim.duckdns.org:19223/getRecruitList')
      .then((response) => {
        this.items = response.data
        eventBus.$emit('listChange', this.items.length);
      })
  },
  methods: {
		viewCount: function(id) {
			console.log(id);
    }
	}
}
</script>