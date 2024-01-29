import {
  Form,
  useNavigate,
  useNavigation,
  useActionData,
  json,
  redirect,
} from 'react-router-dom';

import { useState } from 'react';
import PhotoView from '../Service/Delivery/PhotoView';

import classes from './TradeForm.module.css';

function TradeForm({ method, trade }) {
  const data = useActionData();
  const navigate = useNavigate();
  const navigation = useNavigation();

  const [selectedFiles, setSelectedFiles] = useState([]);

  const isSubmitting = navigation.state === 'submitting';

  function cancelHandler() {
    navigate(-1);
  }

  return (
    <Form method={method} className={classes.form}>
      {data && data.errors && (
        <ul>
          {Object.values(data.errors).map((err) => (
            <li key={err}>{err}</li>
          ))}
        </ul>
      )}
      <h2
        style={{
          marginTop: '4rem',
          borderBottom: 'solid',
          borderColor: '#B2B2B2',
          borderWidth: '1px',
        }}
      >
        글작성
      </h2>
      <article>
        <p>
          <input
            id="title"
            type="text"
            name="title"
            placeholder="제목을 작성해 주세요"
            style={{
              backgroundColor: '#F6F6F6',
              border: 'none',
              outline: 'none',
              borderRadius: '4px',
            }}
            required
          ></input>
        </p>
        <div style={{ fontWeight: 'bold' }}>상세 설정</div>
        <input
          id="cost"
          type="int"
          name="cost"
          placeholder="판매 가격"
          style={{
            backgroundColor: '#F6F6F6',
            border: 'none',
            outline: 'none',
            borderRadius: '4px',
          }}
          required
        />
        <div style={{ marginTop: '0.5rem', marginBottom: '1rem' }}>
          <div style={{ fontWeight: 'bold' }}>거래 장소 지정</div>
          <input
            id="region"
            type="text"
            name="region"
            placeholder="직거래 주소"
            style={{
              backgroundColor: '#F6F6F6',
              border: 'none',
              outline: 'none',
              borderRadius: '4px',
            }}
            required
          />
        </div>
      </article>
      <div
        style={{
          border: 'solid',
          borderWidth: '1px 0 1px 0',
          borderColor: '#B2B2B2',
          paddingTop: '0.5rem',
          paddingBottom: '0.5rem',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'flex-end' }}>
          <div className="m-0 fw-bold">사진 추가</div>
          <div
            style={{
              marginLeft: '0.5rem',
              fontSize: 'small',
              color: '#3FA3CF',
            }}
          >
            특징이 잘 드러나도록 촬영해주세요.
          </div>
        </div>
        <div className="d-flex gap-2  text-center">
          <div className="col-9 d-flex">
            <PhotoView
              selectedFiles={selectedFiles}
              setSelectedFiles={setSelectedFiles}
            />
          </div>
        </div>
      </div>
      <p style={{ marginTop: '0.5rem' }}>
        <label htmlFor="description" style={{ fontWeight: 'bold' }}>
          상세 내용 작성
        </label>
        <textarea
          id="description"
          name="description"
          rows="5"
          required
          style={{
            borderColor: '#B2B2B2',
            borderRadius: '4px',
            resize: 'none',
            outline: 'none',
          }}
        />
      </p>
      <div className={classes.actions}>
        <button type="button" onClick={cancelHandler} disabled={isSubmitting}>
          취소
        </button>
        <button disabled={isSubmitting}>
          {isSubmitting ? 'Submitting...' : '저장'}
        </button>
      </div>
    </Form>
  );
}

export default TradeForm;

export async function action({ request, params }) {
  const formData = await request.formData();
  const method = request.method;

  let url = 'http://localhost:8080/trade';

  if (method === 'PATCH') {
    const tradeId = params.tradeId;
    url += `/${tradeId}`;
  }

  const response = await fetch(url, {
    method: method,
    body: formData,
  });

  if (response.status === 422) {
    return response;
  }

  if (!response.ok) {
    throw json({ message: 'Could not save trade.' }, { status: 500 });
  }

  return redirect('/trade');
}
