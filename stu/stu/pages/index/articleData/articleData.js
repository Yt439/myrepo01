// pages/index/articleData/articleData.js
const request = require('../../../utils/request.js');
Page({

  /**
   * 页面的初始数据
   */
  data: {
    article: {
      title: 'The Power of a Smile',
      content: "A smile is a powerful gesture. It costs nothing but conveys warmth and happiness. When we smile, we uplift others and ourselves. In times of sadness, a smile can soothe the soul. Let's share the magic of a smile with the world.",
      translation: '微笑是一种强大的举动。它无需花费，却能传递温暖和快乐。我们微笑时，不仅振奋他人，也振奋自己。在悲伤时刻，微笑能抚慰心灵。让我们与世界分享微笑的魔力。',
    }
  },
  goBack() {
    wx.navigateBack(); // 返回上一页
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    const id = options.id;
    this.fetchArticle(id);
  },

  fetchArticle(id){
    const param = {
      id:id
    }

    request.post("/findArticlesData",param)
    .then(res=>{
      console.log(res.data.data);
      this.setData({
        article: res.data.data,
      });
    }).catch(res=>{
    })
  },


  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

})