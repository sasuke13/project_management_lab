import React, { useState} from 'react';
import { Link, useNavigate } from 'react-router-dom'; 
import './components/styles.css';
import { useDispatch } from 'react-redux';
import axios from 'axios';
const LOGIN_URL = 'https://f5a6-46-219-228-232.ngrok-free.app/api/v1/authorization/login/';
const Login = () => {

  const dispatch = useDispatch();

  const navigate = useNavigate();
  const [errMsg, setErrMsg] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const handleSuccessfulLogin = (accessToken, refreshToken, email) => {
   
    localStorage.setItem('accessToken', accessToken);
    localStorage.setItem('email', email);
    localStorage.setItem('refreshToken', refreshToken);
}
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        LOGIN_URL,
        { email, password },
        {
          withCredentials: true,
          baseURL: URL,
          headers: {
            "Content-Type": "application/json",
          },
          
        }, 
      );
        console.log(response?.data);
  console.log(response?.access);
  console.log(JSON.stringify(response))
        console.log(JSON.stringify(response?.data));
      
        const accessToken = response?.data?.access;
        const refreshToken = response?.data?.refresh;
        handleSuccessfulLogin(accessToken, refreshToken, email);
        setEmail('');
        setPassword('');
       navigate('/myprofile')
    } catch (err) {
        if (!err?.response) {
            setErrMsg('No Server Response');
        } else if (err.response?.status === 400) {
            setErrMsg('Missing Username or Password');
        } else if (err.response?.status === 401) {
            setErrMsg('Unauthorized');
        } else {
            setErrMsg('Login Failed');
        }
    }
}

 

  return (
    <div className='login-position'>
      <form onSubmit={handleSubmit}>
        <div className="login" style={{height:'400px'}}>
        <h3>Увійдіть у  JOSKA DELIVERY</h3>
          <div>
            <label htmlFor="email">Email:</label><br/>
            <input type="email" id="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)} 
            required style={{width:'300px', height:'22px'}} /> <br/><br/>
          </div>
          <div>
            <label htmlFor="password">Пароль:</label><br/>
            <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} 
            required style={{width:'300px', height:'22px'}} /><br/><br/>
          </div>
           <div>
                <button className='button' style={{height:'33px'}}>Увійти</button>
             <p>Не маєте облікового запису? <Link to="/register" className='button' style={{height:'20px'}} >Зареєструватися</Link></p>
           </div>
           
        </div>
        
      </form>
      
    
  </div>
  );
}

export default Login;
