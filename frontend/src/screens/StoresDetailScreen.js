import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom'
import { Row, Col,Card } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import { listStoreDetails } from '../actions/storeActions';
import { listProducts } from '../actions/productActions';
import Product from '../components/Product';


function StoreDetailScreen(props) {
  // const [store, setStore] = useState(null);
  // const [productList, setProductList] = useState(null);
  const { id } = useParams()
  const dispatch = useDispatch()

  const storeDetails = useSelector(state => state.storeDetails)
  const { error, loading, store } = storeDetails

  const productList = useSelector(state => state.productList)
  const { loading:loadingProducts, error:errorProducts , products } = productList


  useEffect(() => {


            dispatch(listStoreDetails(id))
            dispatch(listProducts())

}, [dispatch])

const storeProducts = products.filter(product => product.store === store.name);





  if (!store) {
    return <div>Loading...</div>;
  }


  return (
    <div>
      <Card md={3}className="my-3 p-3 rounded" style={{ width: '30rem' }}>
            <Card.Title as="h1">
                <strong>{store.name}</strong>
            </Card.Title>
            <Card.Title as="h4">
                <strong>from {store.wilaya}</strong>
            </Card.Title>
            </Card>

      <Row>
        <h4>{store.name}' Books</h4>
            {storeProducts.map(product => (
              <Col key={product._id} sm={5} md={4} lg={4} xl={3}>
                  <Product product={product} />
              </Col>
            ))}
          </Row>


    </div>
  );
}

export default StoreDetailScreen;