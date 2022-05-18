<template>
  <div class="goods_manage">
    <div class="head">
      <div class="text-1">
        <el-checkbox v-model="totalchecked" @click="totalselect" style="padding-left:37%">
          全选</el-checkbox
        >
      </div>
      <div class="text-2">商品信息</div>
      <div class="text-3">单价</div>
      <div class="text-3">数量</div>
      <div class="text-3">金额</div>
      <div class="text-3">操作</div>
    </div>

    <div class="outerline">
      <div class="line">
        <div class="text1">
          <el-checkbox
            v-model="checked1"
            style="padding-top: 60%"
          ></el-checkbox>
        </div>
        <div class="text2">
          <img
            id="img"
            src="../../../../assets/picture/雷曼电吹风机家用理发店大功率负离子护发静音宿舍用学生吹风筒.png"
            alt=""
          />
        </div>
        <div class="text3">
          雷曼电吹风机家用理发店大功率负离子护发静音宿舍用学生吹风筒
        </div>
        <div class="text4">型号：1</div>
        <div class="text5">￥67.90</div>
        <div class="text5">1</div>
        <div class="text5">￥67.90</div>
        <div class="text5">
          <input type="button" value="取消" />
        </div>
      </div>
    </div>

    <div class="outerline">
      <div class="line">
        <div class="text1">
          <el-checkbox
            v-model="checked2"
            style="padding-top: 60%"
          ></el-checkbox>
        </div>
        <div class="text2">
          <img
            id="img"
            src="../../../../assets/picture/唐山金边白色骨瓷杯子家用咖啡杯牛奶杯子大容量陶瓷喝水杯马克杯.png"
            alt=""
          />
        </div>
        <div class="text3">
          唐山金边白色骨瓷杯子家用咖啡杯牛奶杯子大容量陶瓷喝水杯马克杯
        </div>
        <div class="text4">型号：大杯</div>
        <div class="text5">￥40.00</div>
        <div class="text5">1</div>
        <div class="text5">￥40.00</div>
        <div class="text5">
          <input type="button" value="取消" />
        </div>
      </div>
    </div>

    <div class="outerline">
      <div class="line">
        <div class="text1">
          <el-checkbox
            v-model="checked3"
            style="padding-top: 60%"
          ></el-checkbox>
        </div>
        <div class="text2">
          <img
            id="img"
            src="../../../../assets/picture/日系简约黑白镜面LED声控闹钟宿舍床头桌面数字钟温度日历电子钟.jpg"
            alt=""
          />
        </div>
        <div class="text3">
          日系简约黑白镜面LED声控闹钟宿舍床头桌面数字钟温度日历电子钟
        </div>
        <div class="text4">型号：柔光升级版</div>
        <div class="text5">￥46.98</div>
        <div class="text5">1</div>
        <div class="text5">￥46.98</div>
        <div class="text5">
          <input type="button" value="取消" />
        </div>
      </div>
    </div>

    <div class="outerline">
      <div class="line">
        <div class="text1">
          <el-checkbox
            v-model="checked4"
            style="padding-top: 60%"
          ></el-checkbox>
        </div>
        <div class="text2">
          <img
            id="img"
            src="../../../../assets/picture/东南亚进口贝壳筷子玫瑰黑木酸枝木原木无漆日式酒店家用软装实木.jpg"
            alt=""
          />
        </div>
        <div class="text3">
          东南亚进口贝壳筷子玫瑰黑木酸枝木原木无漆日式酒店家用软装实木
        </div>
        <div class="text4">型号：10双</div>
        <div class="text5">￥34.98</div>
        <div class="text5">1</div>
        <div class="text5">￥34.98</div>
        <div class="text5">
          <input type="button" value="取消" />
        </div>
      </div>
    </div>

    <div class="outerline">
      <div id="bottom-line"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      totalchecked: false,
      checked1: false,
      checked2: false,
      checked3: false,
      checked4: false,
    };
  },
  methods: {
    totalselect() {
      if (this.checked1 == false && this.totalchecked == true) {
        this.checked1 = true;
      }
      if (this.checked2 == false && this.totalchecked == true) {
        this.checked2 = true;
      }
      if (this.checked3 == false && this.totalchecked == true) {
        this.checked3 = true;
      }
      if (this.checked4 == false && this.totalchecked == true) {
        this.checked4 = true;
      }
    },
  },
};
</script>

<style scoped>
.head {
  display: flex;
  justify-content: center;
  position: relative;
  top: 10px;
  border-top: 1px solid rgb(182, 184, 185);
}

.text-1 {
  width: 200px;
  font-family: "黑体";
}

.text-2 {
  width: 833px;
  font-family: "黑体";
}

.text-3 {
  width: 166.7px;
  font-family: "黑体";
}

.line {
  height: 120px;
  display: flex;
  justify-content: center;
  position: relative;
  top: 50px;
  border-top: 1px solid rgb(182, 184, 185);
  border-left: 1px solid rgb(182, 184, 185);
  border-right: 1px solid rgb(182, 184, 185);
  background-color: rgba(240, 240, 240, 0.801);
}

.text1 {
  width: 60px;
  padding-top: 10px;
}

.text2 {
  width: 135px;
  padding-top: 10px;
}
.text3 {
  width: 375px;
  padding-top: 10px;
  font-family: "仿宋";
  font-size: 90%;
}
.text4 {
  width: 375px;
  text-align: center;
  padding-top: 10px;
  font-size: 90%;
  color: darkgray;
}
.text5 {
  width: 150px;
  padding-top: 10px;
}
.lastline {
  height: 120px;
  display: flex;
  justify-content: center;
  position: relative;
  top: 50px;
  border-top: 1px solid rgb(182, 184, 185);
}
#img {
  width: 120px;
  height: 100px;
}
</style>