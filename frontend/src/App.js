import React, { useEffect } from 'react';
import { BrowserRouter as Router,  Routes, Route, Navigate } from 'react-router-dom';
import Login from './Login';
import Register from './Register';
import Main from './Main';
import MyOrders from './MyOrders';
import UserProfile from './UserProfile';
import { useAuth } from './AuthService';
import { Provider, useSelector } from 'react-redux';
import store, { useAppDispatch }  from './store';
import CreateOrder from './CreateOrder';
import { getProfile } from './api/auth';
import DeliveryInfoPage from './components/DeliveryInfoPage';
import DeliveryTerms from './components/DeliveryTerms';
import WorkingHours from './components/WorkingHours';
import OurSuccess from './components/OurSuccess';
import ArchiveOrders from './ArchiveOrders';
import DeletedOrders from './DeletedOrders';


function App() {
  return (
    <Provider store={store}>
      <Routes>
        <Route path='/' element={<Main/>} />
        <Route path="register" element={<Register/>} />
        <Route path="/login" element={<Login/>} /> 
        <Route path="/myprofile" element={ <UserProfile /> } />
        <Route path="/orders" element={<MyOrders orders={[]}/>} />
         <Route path="/DeletedOrders" element={<DeletedOrders/>}/>
         <Route path='/ArchiveOrders' element={<ArchiveOrders/>}/>
         <Route path="/createdOrder" element={<CreateOrder/>} />
         <Route path="/delivery" element={<DeliveryInfoPage />} />
         <Route path="/term" element={<DeliveryTerms />} />
         <Route path="/workours" element={<WorkingHours />} />
         <Route path="/oursuccess" element={<OurSuccess />} />
      </Routes>
    </Provider>
  )
}

export default App;
