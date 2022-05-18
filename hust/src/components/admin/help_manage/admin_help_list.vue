<template>
  <div class="help_list">
    <div class="select">
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item label="内容">
          <el-input
            placeholder="内容"
            v-model="content"
            style="width: 200px"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="报酬范围">
          <el-form-item :span="11">
            <el-input
              style="width: 110px"
              placeholder="最低报酬"
              v-model="minprice"
              clearable
            ></el-input>
          </el-form-item>
          <el-form-item class="line" :span="2">-</el-form-item>
          <el-form-item :span="11">
            <el-input
              style="width: 110px"
              placeholder="最高报酬"
              v-model="maxprice"
              clearable
            ></el-input>
          </el-form-item>
        </el-form-item>
        <el-form-item label="求助人">
          <el-input
            placeholder="求助人"
            v-model="indeed"
            style="width: 110px"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="完成情况">
          <el-select
            v-model="situationvalue"
            placeholder="请选择"
            style="width: 110px"
            filterable
          >
            <el-option
              v-for="item in situationoptions"
              :key="item.situationvalue"
              :label="item.label"
              :value="item.situationvalue"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="选择时间">
          <el-date-picker
            v-model="datetimevalue"
            type="datetimerange"
            :picker-options="pickerOptions"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            align="right"
          >
          </el-date-picker>
        </el-form-item>
        <el-button type="primary" plain>查询</el-button>
      </el-form>
    </div>
    <div class="list">
      <el-table :data="help_info" height="650" border style="width: 100%">
        <el-table-column prop="content" label="内容" align="center">
        </el-table-column>
        <el-table-column prop="price" label="报酬" align="center">
        </el-table-column>
        <el-table-column prop="indeed" label="求助人" align="center">
        </el-table-column>
        <el-table-column prop="situation" label="完成情况" align="center">
        </el-table-column>
        <el-table-column prop="s_time" label="需求时间" align="center">
        </el-table-column>
        <el-table-column label="操作" align="center" width="300px">
          <template>
            <el-button type="primary">详细信息</el-button>
            <el-button type="danger">关闭</el-button>　
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
      pickerOptions: {
        shortcuts: [
          {
            text: "最近一周",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近一个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近三个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit("pick", [start, end]);
            },
          },
        ],
      },
      situationoptions: [
        {
          situationvalue: "未完成",
          label: "未完成",
        },
        {
          situationvalue: "已完成",
          label: "已完成",
        },
      ],
      help_info: [],
      content: "",
      minprice: "",
      maxprice: "",
      indeed: "",
      situationvalue: "",
      datetimevalue: "",
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
          that.help_info = data.help_info;
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