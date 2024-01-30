import { useState } from 'react';
import React from 'react';

import { PRIMARY_COLOR } from '../../App';

const SignInForm = () => {
  // 초기값 세팅 - 이름, 이메일, 전화번호, 비밀번호, 비밀번호확인
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirm, setPasswordConfirm] = useState('');

  // 오류메세지 상태 저장
  const [nameMessage, setNameMessage] = useState('');
  const [emailMessage, setEmailMessage] = useState('');
  const [phoneMessage, setPhoneMessage] = useState('');
  const [passwordMessage, setPasswordMessage] = useState('');
  const [passwordConfirmMessage, setPasswordConfirmMessage] = useState('');

  // 유효성 검사
  const [isname, setIsName] = useState(false);
  const [isEmail, setIsEmail] = useState(false);
  const [isPhone, setIsPhone] = useState(false);
  const [isPassword, setIsPassword] = useState(false);
  const [isPasswordConfirm, setIsPasswordConfirm] = useState(false);

  const [selectedButton, setSelectedButton] = useState(null);
  const [serviceButton, setserviceButton] = useState(null);

  const handleButtonClick = (buttonType) => {
    if (selectedButton === 'normal') {
      setserviceButton(null);
    }
    setSelectedButton(buttonType);
  };

  const handleServiceClick = (buttonType) => {
    setserviceButton(buttonType);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // 여기에 로그인 처리 로직을 추가하세요.
  };

  const onChangeName = (e) => {
    const currentName = e.target.value;
    setName(currentName);

    if (currentName.length < 2 || currentName.length > 10) {
      setNameMessage('이름을 입력해주세요');
      setIsName(false);
    } else {
      setNameMessage();
      setIsName(true);
    }
  };

  const onChangeEmail = (e) => {
    const currentEmail = e.target.value;
    setEmail(currentEmail);
    const emailRegExp =
      /^[A-Za-z0-9_]+[A-Za-z0-9]*[@]{1}[A-Za-z0-9]+[A-Za-z0-9]*[.]{1}[A-Za-z]{1,3}$/;

    if (!emailRegExp.test(currentEmail)) {
      setEmailMessage('이메일의 형식이 올바르지 않습니다');
      setIsEmail(false);
    } else {
      setEmailMessage('사용 가능한 이메일 입니다.');
      setIsEmail(true);
    }
  };

  const onChangePhone = (getNumber) => {
    const currentPhone = getNumber;
    setPhone(currentPhone);
    const phoneRegExp = /^01([0|1|6|7|8|9])-?([0-9]{3,4})-?([0-9]{4})$/;

    if (!phoneRegExp.test(currentPhone)) {
      setPhoneMessage('올바른 형식이 아닙니다!');
      setIsPhone(false);
    } else {
      setPhoneMessage('사용 가능한 번호입니다:-)');
      setIsPhone(true);
    }
  };

  const addHyphen = (e) => {
    const currentNumber = e.target.value;
    setPhone(currentNumber);
    if (currentNumber.length == 3 || currentNumber.length == 8) {
      setPhone(currentNumber + '-');
      onChangePhone(currentNumber + '-');
    } else {
      onChangePhone(currentNumber);
    }
  };

  const onChangePassword = (e) => {
    const currentPassword = e.target.value;
    setPassword(currentPassword);
    const passwordRegExp =
      /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;
    if (!passwordRegExp.test(currentPassword)) {
      setPasswordMessage(
        '숫자+영문자+특수문자 조합으로 8자리 이상 입력해주세요!'
      );
      setIsPassword(false);
    } else {
      setPasswordMessage('안전한 비밀번호 입니다.');
      setIsPassword(true);
    }
  };
  const onChangePasswordConfirm = (e) => {
    const currentPasswordConfirm = e.target.value;
    setPasswordConfirm(currentPasswordConfirm);
    if (password !== currentPasswordConfirm) {
      setPasswordConfirmMessage('비밀번호가 일치하지 않습니다.');
      setIsPasswordConfirm(false);
    } else {
      setPasswordConfirmMessage('비밀번호가 일치합니다.');
      setIsPasswordConfirm(true);
    }
  };

  return (
    <>
      <div
        className="container"
        style={{ marginTop: '100px', marginBottom: '100px' }}
      >
        <div className="row justify-content-center">
          <div className="col-md-12">
            <form
              onSubmit={handleSubmit}
              className="rounded p-4 border shadow-sm mx-auto"
              style={{ width: '100%', maxWidth: '70%' }}
            >
              <h2 className="mb-4">Sign In</h2>
              <button
                type="button"
                className={`btn ${
                  selectedButton === 'normal'
                    ? 'btn-primary text-white'
                    : 'btn-outline-primary text-dark'
                } rounded-pill py-3 mx-2`}
                onClick={() => handleButtonClick('normal')}
              >
                일반 가입
              </button>
              <button
                type="button"
                className={`btn ${
                  selectedButton === 'company'
                    ? 'btn-primary text-white'
                    : 'btn-outline-primary text-dark'
                } rounded-pill py-3 mx-2`}
                onClick={() => handleButtonClick('company')}
              >
                업체 가입
              </button>
              <div className="form-group mb-4">
                <label htmlFor="name">Username</label>
                <input
                  id="name"
                  className="form-control rounded-pill py-4"
                  name="name"
                  placeholder="Enter username"
                  required
                  value={name}
                  onChange={onChangeName}
                />
                <p className="message">{nameMessage}</p>
              </div>
              <div className="form-group mb-4">
                <label htmlFor="email">Email</label>
                <input
                  id="email"
                  className="form-control rounded-pill py-4"
                  name="name"
                  value={email}
                  placeholder="Enter email"
                  required
                  onChange={onChangeEmail}
                />
                <p className="message">{emailMessage}</p>
              </div>
              <div className="form-group mb-4">
                <label htmlFor="phone">Phone Number</label>
                <div className="input-group">
                  <input
                    id="phone"
                    name="phone"
                    value={phone}
                    onChange={addHyphen}
                    type="tel"
                    className="form-control rounded-pill py-4"
                    placeholder="Enter phone number"
                    required
                  />
                  <button
                    type="button"
                    className="btn btn-secondary rounded-pill py-3"
                    style={{
                      marginLeft: '-1px',
                      backgroundColor: PRIMARY_COLOR,
                    }}
                  >
                    Send Code
                  </button>{' '}
                  <br />
                  <p className="message">{phoneMessage}</p>
                </div>
              </div>
              <div className="form-group mb-4">
                <label htmlFor="enterCode">Enter Code</label>
                <div className="input-group">
                  <input
                    type="text"
                    className="form-control rounded-pill py-4"
                    id="enterCode"
                    placeholder="Enter code"
                    required
                  />
                  <button
                    type="button"
                    className="btn btn-secondary rounded-pill py-3"
                    style={{
                      marginLeft: '-1px',
                      backgroundColor: PRIMARY_COLOR,
                    }}
                  >
                    Verify Code
                  </button>
                </div>
              </div>
              <div className="form-group mb-4">
                <label htmlFor="password">Password</label>
                <input
                  type="password"
                  className="form-control rounded-pill py-4"
                  name="password"
                  id="password"
                  value={password}
                  onChange={onChangePassword}
                  placeholder="Password"
                  required
                />
                <p className="message">{passwordMessage}</p>
              </div>
              <div className="form-group mb-4">
                <label htmlFor="passwordConfirm">Confirm Password</label>
                <input
                  type="password"
                  className="form-control rounded-pill py-4"
                  id="passwordConfirm"
                  name="passwordConfirm"
                  value={passwordConfirm}
                  onChange={onChangePasswordConfirm}
                  placeholder="Confirm password"
                  required
                />
                <p className="message">{passwordConfirmMessage}</p>
              </div>
              {selectedButton === 'company' && (
                <div className="mt-3">
                  <button
                    type="button"
                    className={`btn ${
                      serviceButton === 'clean'
                        ? 'btn-primary text-white'
                        : 'btn-outline-primary text-dark'
                    } rounded-pill py-3 mx-2`}
                    style={{ minWidth: '120px' }}
                    onClick={() => handleServiceClick('clean')}
                  >
                    청소
                  </button>
                  <button
                    type="button"
                    className={`btn ${
                      serviceButton === 'delivery'
                        ? 'btn-primary text-white'
                        : 'btn-outline-primary text-dark'
                    } rounded-pill py-3 mx-2`}
                    style={{ minWidth: '120px' }}
                    onClick={() => handleServiceClick('delivery')}
                  >
                    용달
                  </button>
                </div>
              )}
              <button
                type="submit"
                className="btn btn-primary rounded-pill py-3"
                style={{
                  width: '100%',
                  marginTop: '5px',
                  marginBottom: '5px',
                  backgroundColor: '#4A3AFF',
                }}
              >
                Sign In
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
};

export default SignInForm;
