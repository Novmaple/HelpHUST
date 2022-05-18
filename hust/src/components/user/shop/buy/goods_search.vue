<template>
  <div class="goods_search">
    <div class="search">
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item>
          <el-input v-model="goodsname" placeholder="请输入内容"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" plain>搜索</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="goods_form">
      <div class="select">
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
          <el-form-item>
            <el-select v-model="distance" filterable placeholder="位置">
              <el-option
                v-for="item in distanceoptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-select v-model="type" filterable placeholder="商品类型">
              <el-option
                v-for="item in typeoptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-select v-model="arrange" filterable placeholder="排序">
              <el-option
                v-for="item in arrangeoptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-select v-model="brand" filterable placeholder="品牌">
              <el-option
                v-for="item in brandoptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-select v-model="time" filterable placeholder="已使用时长">
              <el-option
                v-for="item in timeoptions"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              >
              </el-option>
            </el-select>
          </el-form-item>
        </el-form>
      </div>
      <div class="form">
        <div class="goods1">
          <div class="goods1_image">
            <img
              src="../../../../assets/picture/电竞椅电脑椅家用可躺学生主播游戏座椅办公椅靠背舒适久坐老板椅 (2).png">
          </div>
          <div class="goods1_name">
            电竞椅电脑椅家用可躺学生主播游戏座椅办公椅靠背舒适久坐老板椅
          </div>
          <div class="goods1_price">￥340</div>
        </div>
        <div class="goods2">
          <div class="goods2_image">
            <img
              src="../../../../assets/picture/雷曼电吹风机家用理发店大功率负离子护发静音宿舍用学生吹风筒.png">
          </div>
          <div class="goods2_name">
            雷曼电吹风机家用理发店大功率负离子护发静音宿舍用学生吹风筒
          </div>
          <div class="goods2_price">￥80</div>
        </div>
        <div class="goods3">
          <div class="goods3_image">
            <img
              src="../../../../assets/picture/电脑台式桌转角书桌书架组合家用学生写字台学习桌书柜一体拐角桌.jpg">
          </div>
          <div class="goods3_name">
            电脑台式桌转角书桌书架组合家用学生写字台学习桌书柜一体拐角桌
          </div>
          <div class="goods3_price">￥456</div>
        </div>
        <div class="goods4">
          <div class="goods4_image">
            <img
              src="../../../../assets/picture/RGB灯带装饰自粘显示器氛围灯电视usb5v灯条机箱桌面电脑led变色.jpg">
          </div>
          <div class="goods4_name">
            RGB灯带装饰自粘显示器氛围灯电视usb5v灯条机箱桌面电脑led变色
          </div>
          <div class="goods4_price">￥87</div>
        </div>
        <div class="goods5">
          <div class="goods5_image">
            <img
              src="../../../../assets/picture/东南亚进口贝壳筷子玫瑰黑木酸枝木原木无漆日式酒店家用软装实木.jpg">
          </div>
          <div class="goods5_name">
            东南亚进口贝壳筷子玫瑰黑木酸枝木原木无漆日式酒店家用软装实木
          </div>
          <div class="goods5_price">￥32</div>
        </div>
        <div class="goods6">
          <div class="goods6_image">
            <img
              src="../../../../assets/picture/设计师授权款 “SP 构成 composition ” 升级款防水桌垫.jpg">
          </div>
          <div class="goods6_name">
            设计师授权款 “SP 构成 composition ” 升级款防水桌垫
          </div>
          <div class="goods6_price">￥24</div>
        </div>
        <div class="goods7">
          <div class="goods7_image">
            <img
              src="../../../../assets/picture/唐山金边白色骨瓷杯子家用咖啡杯牛奶杯子大容量陶瓷喝水杯马克杯.png">
          </div>
          <div class="goods7_name">
            唐山金边白色骨瓷杯子家用咖啡杯牛奶杯子大容量陶瓷喝水杯马克杯
          </div>
          <div class="goods7_price">￥30</div>
        </div>
        <div class="goods8">
          <div class="goods8_image">
            <img
              src="../../../../assets/picture/日系简约黑白镜面LED声控闹钟宿舍床头桌面数字钟温度日历电子钟.jpg">
          </div>
          <div class="goods8_name">
            日系简约黑白镜面LED声控闹钟宿舍床头桌面数字钟温度日历电子钟
          </div>
          <div class="goods8_price">￥45</div>
        </div>
        <div class="goods9">
          <div class="goods9_image">
            <img
              src="../../../../assets/picture/空想逻辑 PS4氛围灯电竞房吃豆人装饰灯PS5手柄灯创意桌面光污染.png">
          </div>
          <div class="goods9_name">
            空想逻辑 PS4氛围灯电竞房吃豆人装饰灯PS5手柄灯创意桌面光污染
          </div>
          <div class="goods9_price">￥40</div>
        </div>
        <div class="goods10">
          <div class="goods10_image">
            <img
              src="../../../../assets/picture/桌面草编收纳盒钥匙遥控器手机客厅杂物书桌收纳盒壁挂玄关储物盒.jpg">
          </div>
          <div class="goods10_name">
            桌面草编收纳盒钥匙遥控器手机客厅杂物书桌收纳盒壁挂玄关储物盒
          </div>
          <div class="goods10_price">￥30</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      distanceoptions: [
        {
          value: "选项1",
          label: "紫菘",
        },
        {
          value: "选项2",
          label: "韵苑",
        },
        {
          value: "选项3",
          label: "沁苑",
        }
      ],
      typeoptions: [
        {
          value: "选项1",
          label: "日用品",
        },
        {
          value: "选项2",
          label: "书籍",
        },
        {
          value: "选项3",
          label: "电器",
        }
      ],
      arrangeoptions: [
        {
          value: "选项1",
          label: "升序",
        },
        {
          value: "选项2",
          label: "降序",
        }
      ],
      brandoptions: [
        {
          value: "选项1",
          label: "美的",
        },
        {
          value: "选项2",
          label: "海尔",
        }
      ],
      timeoptions: [
        {
          value: "选项1",
          label: "1个月以下",
        },
        {
          value: "选项2",
          label: "3个月以下",
        },
        {
          value: "选项3",
          label: "6个月以下",
        },
        {
          value: "选项4",
          label: "1年以下",
        },
        {
          value: "选项5",
          label: "1年以上",
        },
      ],
      goodsname: "",
      distance:"",
      type:"",
      arrange:"",
      brand:"",
      time:""
    };
  },
};
</script>

<style scoped>
.search,
.select {
  text-align: center;
}
.select {
  margin-top: 2%;
}
.goods1,
.goods2,
.goods3,
.goods4,
.goods5,
.goods6,
.goods7,
.goods8,
.goods9,
.goods10 {
  float: left;
  margin-left: 4.4%;
  margin-top: 2%;
  height: 30%;
  width: 5%;
}
img{
  width: 100%;
  height: 100%;
}
</style>