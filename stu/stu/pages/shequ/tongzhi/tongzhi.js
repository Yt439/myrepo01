// pages/notification-detail/notification-detail.js
const request = require('../../../utils/request.js');
Page({
  data: {
    notification: {
      id: 1,
      title: '系统通知标题',
      createdAt: '2025-02-01',
      content: '这是通知的详细内容。通知内容可以比较长。',
    },
    comments: [],
    newComment: '', // 存储输入框中的评论内容
    gonggao_id:'',
  },

  // 处理评论输入
  onCommentInput(event) {
    this.setData({
      newComment: event.detail.value,
    });
  },

  // 发布评论
  onPostComment() {
    const { newComment, comments } = this.data;
    console.log(newComment)
    console.log(comments)

    const userInfo = wx.getStorageSync('userInfo');
    param = {
      user_id:userInfo.id,
      announcement:this.data.gonggao_id,
      content:newComment
    }
    request.post("/addPinlun", param)
      .then(res => {
        console.log(res)
        this.findAnnouncement(this.data.gonggao_id)
        this.findPinlun(this.data.gonggao_id)
      })
      .catch(err => {
      });
    
    // 更新评论列表
    this.setData({
      // comments: [newCommentData, ...comments],
      newComment: '', // 清空输入框
    });
  },

  onLoad(options) {
    const id = options.id;
    this.setData({
      gonggao_id:id
    })
    console.log(this.data.gonggao_id)
    this.findAnnouncement(id)
    this.findPinlun(id)
  },
  findAnnouncement(id){
    const param = {
      id:id
    }
    request.post("/findAnnouncementData",param)
    .then(res=>{
      console.log(res.data);
      this.setData({
        notification: res.data.data,
      });
      this.setData({
        announcements: res.data.data,
      });
    }).catch(res=>{
    })
  },
  findPinlun(id){
    const param = {
      announcement:id
    }
    request.post("/findPinlunList",param)
    .then(res=>{
      console.log(res.data);
      this.setData({
        comments: res.data.data,
      });
    }).catch(res=>{
    })
  },

});
