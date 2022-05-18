<template>
<div class="myshop_browse">
    <div style="margin: 2% 2%;background-color:lightgray;height:600px;">
		<p style="padding-top: 20px;padding-left: 20px;">浏览记录</p>
		<hr>
		<div class="track-rcol">
			<div class="track-list">
				<ul>
					<li class="first">
						<span class="time">2021-11-11 18:07:15</span>
						<span class="txt">出售闲置键盘，199购入，因女朋友赠送键盘因此闲置，150可小刀</span>
					</li>
					<li>
						<span class="time">2021-11-10 12:05:21</span>
						<span class="txt">求帮取快递，紫菘13栋快递点，5r</span>
					</li>
					<li>
						<span class="time">2021-11-10 22:54:15</span>
						<span class="txt">求购闲置路由器，预算100</span>
					</li>
					<li>
						<span class="time">2021-11-09 20:25:30</span>
						<span class="txt">紫菘7栋，求帮带美食屋辣子鸡</span>
					</li>
				</ul>
			</div>
		</div>
	</div>
</div>
</template>

<script>
export default {};
</script>

<style scoped>
body {
  font-size: 15px;
}

ul li {
  list-style-type: disc;
}
.track-rcol {
  width: 100%;
}

.track-list li {
  margin-left: 50px;
  margin-top: 80px;
  color: rgb(0, 0, 0);
}

.track-list li.first {
  color: red;
  font-size: 18px;
}

.track-list li .time .txt {
  margin-top: 40px;
  margin-left: 20px;
  position: relative;
  display: inline-block;
}
</style>
