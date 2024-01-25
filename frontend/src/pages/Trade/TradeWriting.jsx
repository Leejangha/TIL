// import TradeForm from '../../components/Trade/TradeForm';
import { useState } from 'react';
import Swiper, { Navigation, Pagination } from 'swiper';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';

// Swiper 사용 설정
Swiper.use([Navigation, Pagination]);

function TradeWriting() {
    const [showImages, setShowImages] = useState([]);

    // 이미지 상대경로 저장
    const handleAddImages = (event) => {
      const imageLists = event.target.files;
      let imageUrlLists = [...showImages];

      for (let i = 0; i < imageLists.length; i++) {
        const currentImageUrl = URL.createObjectURL(imageLists[i]);
        imageUrlLists.push(currentImageUrl);
      }

      if (imageUrlLists.length > 10) {
        imageUrlLists = imageUrlLists.slice(0, 10);
      }

      setShowImages(imageUrlLists);
    };

    // X버튼 클릭 시 이미지 삭제
    const handleDeleteImage = (id) => {
      setShowImages(showImages.filter((_, index) => index !== id));
    };

    return (
      <>
        <div>
          <h1>trade</h1>
          <label
            htmlFor="input-file"
            onChange={handleAddImages}
          >
            <input
              type="file"
              id="input-file"
              multiple
            />
            <span>사진추가</span>
          </label>
          {showImages.map((image, id) => (
            <div key={id}>
              <img src={image} alt={`${image}-${id}`} />
              <button onClick={() => handleDeleteImage(id)}>X</button>
            </div>
          ))}
        </div>
      </>
    );
  };

export default TradeWriting;