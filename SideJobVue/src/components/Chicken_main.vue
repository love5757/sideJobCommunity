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
							<button class="item-btn">Detail</button>
						</div>
					</div>
				</div>
			</div>	
		</div>
	</div>
</template>
<script>

export default {
  name: 'chickenMain',
  data () {
    return {
      items: [
		  {contents: 'item'}
	  ]
    }
}
}
</script>
<script src="../scripts/company_data.js"/>

