<template>
  <div class="myhelp_publish">
    <div id="head0">
      <h1>我的发布</h1>
    </div>
    <div id="head2">
      <table border="2">
        <td>
          <form>
            <input
              type="button"
              value="已完成"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
        <td>
          <form>
            <input
              type="button"
              value="未完成"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
      </table>
    </div>

    <table border="big">
      <tr class="one">
        <th width="16%" height="80px" style="font-size: 150%">发布时间</th>
        <th width="16%" style="font-size: 150%">互助类型</th>
        <th width="22%" style="font-size: 150%">互助描述</th>
        <th width="16%" style="font-size: 150%">价格</th>
        <th width="34%" style="font-size: 150%">顾客评价</th>
      </tr>

      <tr>
        <td height="80px">……</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td height="80px">……</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td height="80px">……</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
      <tr>
        <td height="40px">……</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
      </tr>
    </table>
    <div id="head1">
      <p style="text-align: center">Hust.帮</p>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
#head0 {
  background-color: rgb(240, 230, 230);
  color: rgb(37, 4, 4);
  border: 1px solid rgb(26, 6, 6);
  height: 80px;
}
#head1 {
  background-color: rgb(43, 3, 3);
  color: white;
  border: 1px solid rgb(26, 6, 6);
  text-align: center;
  margin-top: 1%;
  height: 50px;
}
#head2 {
  height: 80px;
  text-align: center;
}
.caption {
  text-align: center;
  font-family: "宋体";
  font-size: 200%;
  font-weight: 1000;
  letter-spacing: 20px;
}
#time {
  font-weight: 300px;
}
.slow {
  text-align: right;
  color: blue;
}
#slowy {
  text-align: right;
  color: blue;
}
table {
  font-size: 16px;
  text-align: center;
  margin: 3px auto;
  width: 60%;
}
</style>