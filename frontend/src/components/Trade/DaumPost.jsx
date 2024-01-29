import { useDaumPostcodePopup } from "react-daum-postcode";

function DaumPost(setAddressObj) {
  const open = useDaumPostcodePopup(setAddressObj);
  console.log(setAddressObj)

  const handleComplete = (data) => {
    let fullAddress = data.address;
    let extraAddress = '';
    let localAddress = data.sido + ' ' + data.sigungu;

    if (data.addressType === 'R') {
      if (data.bname !== '') {
        extraAddress += data.bname;
      }
      if (data.buildingName !== '') {
        extraAddress += extraAddress !== '' ? `, ${data.buildingName}` : data.buildingName;
      }

      fullAddress = fullAddress.replace(localAddress, '');
      fullAddress += extraAddress !== '' ? `(${extraAddress})` : '';

      props.setAddressObj({
        areaAddress: localAddress,
        townAddress: fullAddress
      });

      // If you need to use setLocationObj, add the relevant code here
    }
  };

  const handleClick = () => {
    open({ onComplete: handleComplete });
  };

  return (
    <button type="button" onClick={handleClick}>
      Find address
    </button>
  );
}

export default DaumPost;
