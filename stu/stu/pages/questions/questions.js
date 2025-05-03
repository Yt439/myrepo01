// pages/questions/questions.js
const request = require('../../utils/request.js');

Page({

  /**
   * 页面的初始数据
   */
  data: {
    currentIndex: 0, // 当前题目索引
    answeredCount: 0, // 已答题目数
    questions: [],
    Answers_data:'',
    number_data:'',
    yes_count:'',
    no_count:'',
    showDialog:false
  },

  findquestion(){
    const userInfo = wx.getStorageSync('userInfo');
    param = {
      user_id:userInfo.id
    }
    request.post("/findQuestionList", param)
      .then(res => {
        console.log(res)
        console.log(res.data.number)
        this.setData({
          questions:res.data.data,
          number_data:res.data.number
        })
        console.log(this.number_data)
      })
      .catch(err => {
      });
  },
  
  onAnswer(e) {
    const index = e.currentTarget.dataset.index; // 获取用户选择的选项索引
    const answer = e.currentTarget.dataset.answer
    const param = {
      choose_id:index,
      answer_id:answer
    }
    request.post("/updateAnswers",param)
      .then(res => {
        console.log(res)
      })
      .catch(err => {
      });
    this.nextQuestion();
  },
  
  nextQuestion() {
    if (this.data.currentIndex < this.data.questions.length - 1) {
      this.setData({
        answeredCount:this.data.answeredCount + 1,
        currentIndex: this.data.currentIndex + 1,// 跳转到下一题
      });
    } else {
      // 如果是最后一题，答完后退出
      const userInfo = wx.getStorageSync('userInfo');
    param = {
      user_id:userInfo.id,
      number:this.data.number_data
    }
    console.log(param)
    request.post("/select_score", param)
      .then(res => {
        console.log(res.data)
        this.setData({
          yes_count:res.data.data.yes_count,
          no_count:res.data.data.no_count,
          showDialog: true,
        })
        
      })
      .catch(err => {
      });
    }
  },

  onConfirm() {
    console.log('点击111');
    console.log(this.data.number_data)
    wx.navigateTo({
      url: `/pages/user/jilu/jilu?number=${this.data.number_data}`,
    });
    // this.setData({ showDialog: false });
  },

  // 新增方法处理 dialog 取消
  onCancel() {
    wx.switchTab({
      url: '/pages/index/index'
    });
    this.setData({ showDialog: false });
  },
 

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.findquestion();
  },
  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },


})