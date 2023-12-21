import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import './components/styles.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

const UserProfile = () => {
  function isUserAuthenticated() {
    const accessToken = localStorage.getItem('accessToken');
    return !!accessToken; 
  }
  if (!isUserAuthenticated()) {
    // Немає токена, перенаправлення на сторінку авторизації
    window.location.href = '/login';
  }
  const accessToken = localStorage.getItem('accessToken');
  const refreshToken = localStorage.getItem('refreshToken');
  const CHANGEINFO_URL='https://f5a6-46-219-228-232.ngrok-free.app/api/v1/authorization/update_user/';
  const [surname, setSurname]=useState('');
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [email, setEmail] = useState("");
  const [phone_number, setPhoneNumber] = useState("");
  const [data, setData] = useState([]);
  const [ChangeInfo, setChangeInfo] = useState(false);
  const [password, setPassword]=useState("");
  const navigate=useNavigate();
  const handleSaveClick = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.put(CHANGEINFO_URL,
        { name, email, password, phone_number },
        {
          withCredentials: true,
          baseURL: URL,
          headers: {
            Authorization: `Bearer ${accessToken}`,
            "Content-Type": "application/json",
          },
          
        }
      );
      console.log(response?.data);
      const updatedResponse = await axios.get('https://f5a6-46-219-228-232.ngrok-free.app/api/v1/authorization/user/',{
        withCredentials: true,
        baseURL: URL,
        headers: {
          Authorization: `Bearer ${accessToken}`,
          "Content-Type": "application/json",
        },
        
      } )
      .then(response => {
        console.log('Профіль користувача:', response.data);
        setData(response.data)
  
      })


      setChangeInfo(false);
      
    } catch (err) {
      if (!err?.response) {
    }
  }
}
  

  useEffect(() => {
    axios.get('https://f5a6-46-219-228-232.ngrok-free.app/api/v1/authorization/user/',{
      withCredentials: true,
      baseURL: URL,
      headers: {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
      },
      
    })
    .then(response => {
      console.log('Профіль користувача:', response.data);
      setData(response.data)

    })
    .catch(error => {
      console.error('Помилка при отриманні профілю користувача:', error);
    });
  }, []);


  const handleEditClick = () => {
    setChangeInfo(!ChangeInfo);
  
    if (!ChangeInfo) {
    
      setName(data.name);
      setSurname(data.surname);
      setPhoneNumber(data.phone_number);
      setEmail(data.email);
      setAddress(data.address);
    }
    
  };
  const handleMain = async () => {
        
    navigate('/');
};
  const handleLogout = async () => {
      
    localStorage.removeItem('email');
    localStorage.removeItem('accessToken');
    localStorage.removeItem('refreshToken');
    
    navigate('/');
};
 
  const handleCancelClick = () => {

      setChangeInfo(false); 
    };


  return (
    <div >
      
      <div className="row nav-logout" style={{ display: 'flex', flexDirection: 'row' }}>
        <nav class="navbar navbar-expand-sm bg-dark navbar-dark ">
          <div className="row" style={{ display: 'flex', flexDirection: 'row', width: '100%' }}>
            <div className="col" style={{ paddingTop: '15px', width: '100%', textAlign: 'left', alignItems:'flex-end' }}>
              <Link to="/" style={{marginLeft: 0}}>
                <img src="star1.png" alt="star" width="290" height="90" />
              </Link>
            </div>

            <div className="col" style={{ padding: '25px', width: '40%', textAlign: 'right' }}>
               <button className="button" style={{ height: '40px' }} onClick={handleLogout} >Вихід</button> 
            </div>
            <div className='col' style={{ padding: '25px', width: '10%' }}>
              <img src="support.png" alt="star" width="70" height="60" style={{ borderRadius: '100px' }} ></img>
            </div>

          </div>
        </nav>
      </div>

      <div className="row d-flex justify-content-center" style={{ display: 'flex', flexDirection: 'row' }}>
        <div className="vertical-menu">
          <Link to="/myprofile" className="menu-item" style={{ background: 'lightgray' }}>
            Мій профіль
          </Link>
          <Link to="/orders" className="menu-item">
            Мої замовлення
          </Link>
          <Link to="/createdOrder" className="menu-item">
            Створити посилку
          </Link>
          <Link to="/ArchiveOrders" className="menu-item">
            Архівовані
          </Link>
          <Link to="/DeletedOrders" className="menu-item">
            Видалені
          </Link>
        </div>
        <div className="col user-profile " style={{}}>
          <div>
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Sample_User_Icon.png" alt="timer" className="rounded-image" style={{ width: '90px', height: '100px' }} />
          </div>
          {ChangeInfo ? (
            <div className='change-info'>
              <form onSubmit={handleSaveClick}>
              <h3>Змінити інформацію профілю:</h3>
              <strong>Ім'я: </strong>
              <input type="text" id="name" name="name" value={name} onChange={(e) => setName(e.target.value)}
              style={{marginTop:'10px',marginLeft:'110px'}}/>
             <br/>
             <strong>Пароль: </strong>
             <input type="password" id="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} 
              style={{marginTop:'10px',marginLeft:'80px'}}/>
             <br/>
             <strong>Номер телефону: </strong>
             <input type="number" id="phone_number" name="phone_number" value={phone_number} onChange={(e) => setPhoneNumber(e.target.value)} 
              style={{marginTop:'10px'}}/>
             <br/>
             <strong>Email: </strong>
             <input type="email" id="email" name="email" value={email} onChange={(e) => setEmail(e.target.value)}
              style={{marginTop:'10px',marginLeft:'100px'}} />
             <br/>
             <strong>Адреса: </strong>
             <input type="text" id="address" name="address" value={address} onChange={(e) => setAddress(e.target.value)} 
              style={{marginTop:'10px', marginBottom:'30px',marginLeft:'90px'}}/>
             <br/>
             <button onClick={handleCancelClick} className='button' style={{height:'33px', width:'200px'}}>Скасувати</button>
             <button type="submit" className='button' style={{height:'33px', width:'200px'}}>Зберегти зміни</button>
             </form>
             </div>
          ) : (
            
            <div>
              <h3>ТВІЙ ПРОФІЛЬ </h3>
              <div >
                <h4>{data.name} {data.surname}</h4>
              </div>
              <div>
                <strong>Номер телефону:</strong> {data.phone_number}
              </div>
              <br />
              <div>
                <strong>Email:</strong> {data.email}
              </div>
              <br />
              <div>
                <strong>Адреса:</strong> {data.address}
              </div>
              <br />
              <button className="button" onClick={handleEditClick} style={{height:'40px', width:'200px'}}>Змінити інформацію</button>
            </div>
          )}
        </div>
      </div>
    </div>
)};

export default UserProfile;