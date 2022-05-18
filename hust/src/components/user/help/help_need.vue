<template>
  <div class="help_need">
    <div id="head0">
      <h1>我的需求</h1>
    </div>

    <div id="head1">
      <table border="2">
        <td>
          <form>
            <input
              type="button"
              value="已发布"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
        <td>
          <form>
            <input
              type="button"
              value="已接受"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
        <td>
          <form>
            <input
              type="button"
              value="未付款"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
        <td>
          <form>
            <input
              type="button"
              value="已付款"
              style="height: 40px; width: 100px"
            />
          </form>
        </td>
      </table>
    </div>

    <div id="head2">
      <table border="big">
        <tr class="">
          <th width="12%" height="80px" style="font-size: 150%">任务名称</th>
          <th width="16%" style="font-size: 150%">任务介绍</th>
          <th width="11%" style="font-size: 150%">剩余时长</th>
          <th width="22%" style="font-size: 150%">详情</th>
        </tr>
        <tr>
          <td height="80px">……</td>
          <td></td>
          <td></td>
          <td>
            <p class="slow">
              <a href="https//www.baidu.com" title="查看">查看</a>
            </p>
          </td>
        </tr>
        <tr>
          <td height="80px">……</td>
          <td></td>
          <td></td>
          <td>
            <p class="slow">
              <a href="https//www.baidu.com" title="查看">查看</a>
            </p>
          </td>
        </tr>
        <tr>
          <td height="80px">……</td>
          <td></td>
          <td></td>
          <td>
            <p class="slow">
              <a href="https//www.baidu.com" title="查看">查看</a>
            </p>
          </td>
        </tr>
        <tr>
          <td height="40px">……</td>
          <td></td>
          <td></td>
          <td>
            <p class="slow">
              <a href="https//www.baidu.com" title="查看">查看</a>
            </p>
          </td>
        </tr>
      </table>
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
  height: 80px;
}
#head2 {
  height: 80px;
}

table {
  font-size: 16px;
  text-align: center;
  margin: 3px auto;
  width: 60%;
}
</style>