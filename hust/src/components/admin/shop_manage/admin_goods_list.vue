<template>
  <div class="goods_list">
    <div class="select">
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item label="商品名称">
          <el-input
            placeholder="商品名称"
            v-model="name"
            style="width: 200px"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="价格范围">
          <el-form-item style="width: 110px">
            <el-input
              placeholder="最低价格"
              v-model="minprice"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item class="line" :span="2">-</el-form-item>
          <el-form-item style="width: 110px">
            <el-input
              placeholder="最高价格"
              v-model="maxprice"
              clearable
            ></el-input>
          </el-form-item>
        </el-form-item>
        <el-form-item label="类型">
          <el-select
            v-model="typevalue"
            placeholder="请选择"
            style="width: 110px"
            filterable
          >
            <el-option
              v-for="item in typeoptions"
              :key="item.typevalue"
              :label="item.label"
              :value="item.typevalue"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="选择时间">
          <el-date-picker
            style="width: 140px"
            v-model="datevalue"
            align="right"
            type="date"
            placeholder="选择日期"
            :picker-options="pickerOptions"
          >
          </el-date-picker>
        </el-form-item>
        <el-button type="primary" plain>查询</el-button>
      </el-form>
    </div>
    <div class="list">
      <el-table :data="goods_info" height="650" border style="width: 100%">
        <el-table-column prop="name" label="商品名称" align="center">
        </el-table-column>
        <el-table-column prop="price" label="价格" align="center">
        </el-table-column>
        <el-table-column prop="type" label="类型" align="center">
        </el-table-column>
        <el-table-column prop="s_time" label="上架时间" align="center">
        </el-table-column>
        <el-table-column label="操作" align="center" width="300px">
          <template>
            <el-button type="primary">详细信息</el-button>
            <el-button type="danger">下架</el-button>　
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      typeoptions: [
        {
          typevalue: "日用品",
          label: "日用品",
        },
        {
          typevalue: "电器",
          label: "电器",
        },
        {
          typevalue: "书籍",
          label: "书籍",
        },
      ],
      goods_info: [],
      pickerOptions: {
        disabledDate(time) {
          return time.getTime() > Date.now();
        },
        shortcuts: [
          {
            text: "今天",
            onClick(picker) {
              picker.$emit("pick", new Date());
            },
          },
          {
            text: "昨天",
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24);
              picker.$emit("pick", date);
            },
          },
          {
            text: "一周前",
            onClick(picker) {
              const date = new Date();
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit("pick", date);
            },
          },
        ],
      },
      name: "",
      minprice: "",
      maxprice: "",
      typevalue: "",
      datevalue: "",
    };
  },
  mounted() {
    this.getdata();
  },
  methods: {
    getdata() {
      var that = this;
      $.ajax({
        type: "get", //请求方式,默认值GET
        data: "", //请求参数，自动转换为字符串格式，如果是get请求，会自动拼接到url上面
        url: "http://218.197.209.26:8081/data", //请求地址
        context: document.body, //绑定回调中的this
        async: true, //是否是异步请求，默认情况下都是true,如果要发送同步请求，则改为false
        cache: false, //是否返回此页面，默认值为true
        dataType: "json",
        jsonp: "callback", //在一个jsonp请求中重写回调函数的名字。
        //规定预期的服务器响应的数据类型。默认执行智能判断（xml、json、script 或 html）。
        contentType: "application/x-www-form-urlencoded", //发送数据至服务器内容编码类型
        success: function (data) {
          that.goods_info = data.goods_info;
        },
      });
    },
  },
};
</script>

<style scoped>
.select {
  text-align: center;
}

.list {
  margin-top: 2%;
}
.s_list {
  height: 60%;
  width: 80%;
}
</style>