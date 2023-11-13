<template>
    <div>
      <h1>동영상 상세 정보</h1>
      <div>
        <h2>{{ video.snippet.title }}</h2>
        <iframe
          width="560"
          height="315"
          :src="'https://www.youtube.com/embed/' + videoId"
          frameborder="0"
          allowfullscreen
        ></iframe>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRoute } from 'vue-router'
  import axios from 'axios'
  
  const route = useRoute()
  const video = ref({});
  const videoId = route.params.videoId
  
  onMounted(async () => {
    try {
      const response = await axios.get('https://www.googleapis.com/youtube/v3/videos', {
        params: {
          part: 'snippet',
          id: videoId,
          key: 'AIzaSyBg3R3dXkMOONCXoZAcvY6ypCHC-JuDx1M',
        },
      });
  
      video.value = response.data.items[0];
    } catch (error) {
      console.error('YouTube API 요청 중 에러 발생:', error);
    }
  });
  </script>
  
  <style scoped>
  /* 필요한 경우 스타일링을 추가하세요. */
  </style>
  