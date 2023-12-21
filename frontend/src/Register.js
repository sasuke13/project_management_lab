import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import "./Register.css"

function Register() {
  const REGISTER_URL = 'http://localhost:80/api/v1/authorization/register/'
  const dispatch = useDispatch();

  const navigate = useNavigate();
  const [surname, setSurname] = useState('');
  const [errMsg, setErrMsg] = useState('');
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [phone_number, setPhoneNumber] = useState("");
  const [showSuccessModal, setShowSuccessModal] = useState(false);
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(REGISTER_URL,
        { name, surname, email, password, phone_number, address },

      );
      console.log(response?.data);
      console.log(response?.accessToken);
      console.log(JSON.stringify(response))
 
      setName('');
      setSurname('');
      setEmail('');
      setPassword('');
      setAddress('');
      setPhoneNumber('');
      setShowSuccessModal(true);
    } catch (err) {
      if (!err?.response) {
        setErrMsg('No Server Response');
      } else if (err.response?.status === 409) {
        setErrMsg('Username Taken');
      } else {
        setErrMsg('Registration Failed')
      }
    }
  }

  const closeModal = () => {
    setShowSuccessModal(false);
    navigate('/login');
  };

  return (
    <div className='login-position' >
      <form onSubmit={handleSubmit}>
        <div className="login" style={{height:'750px'}}>
          <h2>Реєстрація на сайті JOSKA DELIVERY</h2>
          <div>
            <label htmlFor="name">Ім'я :</label><br />
            <input type="text" id="name" name="name" value={name} onChange={(e) => setName(e.target.value)}
              required style={{ width: '300px', height: '22px' }} /><br /><br />
          </div>
          <div>
            <label htmlFor="surname">Прізвище:</label><br />
            <input type="text" id="surname" name="surname" value={surname} onChange={(e) => setSurname(e.target.value)}
              required style={{ width: '300px', height: '22px' }} /><br /><br />
          </div>
          <div>
            <label htmlFor="email">Електронна адреса:</label><br />
            <input type="email" id="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)}
              required style={{ width: '300px', height: '22px' }} /><br /><br />
          </div>
          <div>
            <label htmlFor="phone_number">Номер телефону :</label><br />
            <input type="text" id="phone_number" name="phone_number" value={phone_number} onChange={(e) => setPhoneNumber(e.target.value)}
              required style={{ width: '300px', height: '22px' }} /><br /><br />
          </div>
          <div>
            <label htmlFor="surname">Адреса:</label><br />
            <input type="text" id="address" name="address" value={address} onChange={(e) => setAddress(e.target.value)}
              required style={{ width: '300px', height: '22px' }} /><br /><br />
          </div>
          <div>
            <label htmlFor="new-password">Пароль:</label><br />
            <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)}
              required style={{ width: '300px', height: '22px' }} /><br /><br />
          </div>
          <div>
            <button type="submit" className='button' style={{ height: '33px', width: '200px' }}>Зареєструватися</button>
            <p>Вже маєте обліковий запис? <Link to="/login" className='button' style={{ height: '20px' }}>Увійти</Link></p>
          </div>
        </div>
      </form>
      {showSuccessModal && (
        <div className="modal-overlay">
          <div className="modal">
            <p style={{ color: 'white' }}>Реєстрація пройшла успішно</p>
            <h3 onClick={closeModal}><u style={{ color: 'white' }}>Перейти до авторизації!</u></h3>
          </div>
        </div>
      )}
    </div>
  );
}

export default Register;