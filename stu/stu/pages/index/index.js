// index.js
const defaultAvatarUrl = 'https://mmbiz.qpic.cn/mmbiz/icTdbqWNOwNRna42FI242Lcia07jQodd2FJGIYQfG0LAJGFxM4FbnQP6yfMxBgJ0F3YRqJCJ1aPAK2dQagdusBZg/0'
const request = require('../../utils/request.js');
Page({


  navigateToWordLearning() {
    console.log('navigateToWordLearning');
    wx.navigateTo({
      url: '/pages/index/wordLevel/wordLevel',  // 跳转到单词学习页面
    });
  },

  navigateToArticleLearning() {
    wx.navigateTo({
      url: '/pages/index/articleList/articleList',  // 跳转到英语文章学习页面
    });
  },

  navigateToDictationLearning() {
    wx.navigateTo({
      url: '/pages/questions/questions',  // 跳转到单词听写页面
    });
  },

  data: {
    motto: 'Hello World',
    userInfo: {
      avatarUrl: defaultAvatarUrl,
      nickName: '',
    },
    hasUserInfo: false,
    userInfo:{},
    canIUseGetUserProfile: wx.canIUse('getUserProfile'),
    canIUseNicknameComp: wx.canIUse('input.type.nickname'),
  },

  onShow(options) {
    this.findUser();
  },

  findUser(){
    const userInfo = wx.getStorageSync('userInfo');
    param = {
      user_id:userInfo.id
    }
    request.post("/FindUserView", param)
      .then(res => {
        console.log(res.data)
        this.setData({
          userInfo: {
            ...res.data,
            img: 'http://localhost:8000' + res.data.img  // 拼接成完整地址
          }
        })
        console.log(this.data.userInfo)
      })
      .catch(err => {
      });
  },
  bindViewTap() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onChooseAvatar(e) {
    const { avatarUrl } = e.detail
    const { nickName } = this.data.userInfo
    this.setData({
      "userInfo.avatarUrl": avatarUrl,
      hasUserInfo: nickName && avatarUrl && avatarUrl !== defaultAvatarUrl,
    })
  },
  onInputChange(e) {
    const nickName = e.detail.value
    const { avatarUrl } = this.data.userInfo
    this.setData({
      "userInfo.nickName": nickName,
      hasUserInfo: nickName && avatarUrl && avatarUrl !== defaultAvatarUrl,
    })
  },
  getUserProfile(e) {
    wx.getUserProfile({
      desc: '展示用户信息', 
      success: (res) => {
        console.log(res)
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    })
  },
})
