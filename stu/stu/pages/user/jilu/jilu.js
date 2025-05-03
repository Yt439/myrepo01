// pages/user/jilu/jilu.js
const request = require('../../../utils/request.js');

Page({
  data: {
    records: [],
    currentIndex: 0
  },

  onLoad(options) {
    const number = options.number;
    this.findData(number);
  },

  findData(number) {
    const userInfo = wx.getStorageSync('userInfo');
    const param = {
      user_id: userInfo.id,
      numbers: number
    };
    request.post("/findAnswersData", param)
      .then(res => {
        this.setData({
          records: res.data.data || []
        });
        console.log(this.data.records)
      })
      .catch(err => {
        console.error("获取答题记录失败", err);
      });
  },

  onOptionClick(e) {
    const optionId = e.currentTarget.dataset.id;
    console.log("Option clicked:", optionId);
    // 你可以在这里做其他的操作，比如显示选项的详细信息
  },

  getOptionClass(item) {
    let className = '';
    if (item.id === item.user_choose) {
      className = 'user-choice'; // 用户选择的选项
    }
    if (item.correct_option) {
      className += ' correct-option'; // 正确的选项
    }
    return className;
  }


});
