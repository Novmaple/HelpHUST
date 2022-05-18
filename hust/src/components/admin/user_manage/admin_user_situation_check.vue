<template>
  <div class="user_situation_list">
    <el-dialog
      title="个人信息"
      :visible.sync="dialogVisible"
      width="90%"
      @close='closeDialog'
    >
      <inf></inf>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false"
          >确 定</el-button
        >
      </span>
    </el-dialog>
    <div class="select">
      <el-form :inline="true" :model="formInline" class="demo-form-inline">
        <el-form-item label="姓名">
          <el-input
            placeholder="姓名"
            v-model="name"
            style="width: 110px"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="学号">
          <el-input
            placeholder="学号"
            v-model="snumber"
            style="width: 180px"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="专业">
          <el-input
            placeholder="专业"
            v-model="academy"
            style="width: 150px"
            clearable
          ></el-input>
        </el-form-item>
        <el-form-item label="选择时间">
          <el-date-picker
            style="width: 300px"
            v-model="datevalue"
            type="daterange"
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
      <el-table :data="user_info" height="650" border style="width: 100%">
        <el-table-column prop="name" label="姓名" align="center">
        </el-table-column>
        <el-table-column prop="snumber" label="学号" align="center">
        </el-table-column>
        <el-table-column prop="academy" label="专业" align="center">
        </el-table-column>
        <el-table-column prop="applydate" label="申请日期" align="center">
        </el-table-column>
        <el-table-column label="操作" align="center" width="300px">
          <template>
            <el-button type="primary" @click="dialogVisible = true"
              >详细信息</el-button
            >
            <el-button type="success">通过</el-button>
            <el-button type="danger">不通过</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import identityinformation from "../../user/identiity/basicInformation.vue";
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
      user_info: [],
      name: "",
      snumber: "",
      academy: "",
      datevalue: "",
      dialogVisible: false,
    };
  },
  mounted() {
    this.getdata();
  },
  components: {
    inf: identityinformation,
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
          that.user_info = data.user_info;
        },
      });
    },
    closeDialog() {
	      this.dialogVisible = false
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