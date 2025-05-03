// pages/index/wordData/wordData.js
const request = require('../../../utils/request.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    word: {},
    words: [],
  },
  onLoad(options) {
    const wordId = options.id;
    this.updateWordDetails(wordId);
  },

  onWordClick(e) {
    const word = e.target.dataset.word; 
    this.playAudio(word);
  },
  playAudio(text) {
    const innerAudioContext = wx.createInnerAudioContext();

    const audioUrl = `http://127.0.0.1:8000/datamp/?text=${encodeURIComponent(text)}`;
    innerAudioContext.src = audioUrl;
    innerAudioContext.play();
    innerAudioContext.onPlay(() => {
      console.log('开始播放语音');
    });

    innerAudioContext.onError((res) => {
      console.error('语音播放错误', res);
    });
  },
  updateWordDetails(wordId) {
    const param = {
      id:wordId
    }
    request.post("/findThesaurusData",param)
    .then(res=>{
      this.setData({
        word: res.data.data,
      });
      // console.log(this.stores)
    }).catch(res=>{
    })
    // this.setData({ word });
  },
  goToPreviousWord(e) {
    const word = e.target.dataset.word; 
    const param = {
      id:word
    }
    this.updateWordDetails(word);
  },
  goToNextWord(e) {
    const word = e.target.dataset.word; 
    this.updateWordDetails(word);
  },

  /**
   * 生命周期函数--监听页面加载
   */

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})