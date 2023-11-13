<template>
    <div>
      <h1>검색 페이지</h1>
  
      <input v-model="searchQuery" placeholder="검색어를 입력하세요" />
      <button @click="searchVideos">검색</button>
  
      <div v-for="video in videos" :key="video.id" @click="goToDetail(video.id.videoId)">
        <img :src="video.snippet.thumbnails.default.url" alt="Thumbnail">
        <h2>{{ video.snippet.title }}</h2>
      </div>
    </div>
  </template>
  
<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const videos = ref([]);
const searchQuery = ref('');

const fetchYouTubeVideos = async () => {
try {
    const response = await axios.get('https://www.googleapis.com/youtube/v3/search', {
    params: {
        part: 'snippet',
        q: searchQuery.value,
        type: 'video',
        key: 'AIzaSyBg3R3dXkMOONCXoZAcvY6ypCHC-JuDx1M',
    },
    });

    videos.value = response.data.items;
} catch (error) {
    console.error('YouTube API 요청 중 에러 발생:', error);
}
};

const goToDetail = (videoId) => {
// VideoId를 기반으로 Detail 페이지로 이동
router.push({ name: 'Detail', params: { videoId } });
};


const searchVideos = async () => {
// 검색 버튼 클릭 시 YouTube API로 동영상을 검색
console.log('검색 버튼 클릭!');
await fetchYouTubeVideos();
};
</script>

<style scoped>
/* 필요한 경우 스타일링을 추가하세요. */
</style>
  