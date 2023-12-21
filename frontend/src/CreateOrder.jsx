import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom'; 
import './components/styles.css';
import { useAppDispatch } from './store';
import { useEffect } from 'react';
import axios from 'axios';
function CreateOrder() {
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
    const dispatch = useAppDispatch();
const [data, setData]=useState('');
    const [orderData, setOrderData] = useState({
        id: '',
        title: '',
        description: '',
        price: '',
        adress: '',
      });
const navigate=useNavigate();
      const handleLogout = async () => {
        
          
          localStorage.removeItem('email');
          localStorage.removeItem('accessToken');
          localStorage.removeItem('refreshToken');
          
      
          
          navigate('/');
      };

      useEffect(() => {
        axios.get('http://localhost:80/api/v1/authorization/user/',{
          withCredentials: true,
          baseURL: URL,
          headers: {
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
      const handleInputChange = (e) => {
        const { name, value } = e.target;
        setOrderData((prevData) => ({ ...prevData, [name]: value }));
      };
      const axiosInstance = axios.create({
        baseURL: 'http://localhost:80/api/v1/orders/',
        withCredentials: true,
        headers: {
          Authorization: `Bearer ${accessToken}`,
          'Content-Type': 'application/json',
        },
      });
      const buttonCreateOrder = async () => {
        try {
          const response = await axiosInstance.post('create/', {
            
          });
      
          console.log('Order created successfully:', response.data);
          
        } catch (error) {
          console.error('Error creating order:', error);
          
        }
      };
      const handleMain = async () => {
        
        navigate('/');
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

<div className="row d-flex justify-content-center" style={{ display: 'flex', flexDirection: 'row' } }>
  <div className="vertical-menu">
  <Link to="/myprofile" className="menu-item" >
      Мій профіль
    </Link>
    <Link to="/orders" className="menu-item">
      Мої замовлення
    </Link>
    <Link to="/createdOrder" className="menu-item" style={{background:'lightgray'}}>
      Створити посилку
    </Link>
    <Link to="/ArchiveOrders" className="menu-item">
            Архівовані
          </Link>
          <Link to="/DeletedOrders" className="menu-item">
            Видалені
          </Link>
  </div>
  <div className="order-container">
      <h3>Для створення посилки, натисніть кнопку нижче</h3>
      <button  className="button" style={{height:'35px'}} onClick={buttonCreateOrder}>Створити </button>
    </div>

</div>
</div>
  );
}

export default CreateOrder;
