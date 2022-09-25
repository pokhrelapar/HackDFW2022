// import React, { Component, useState } from 'react';

// class Card extends React.Component {
// 	render() {
// 		return <div>
// 			<div class="card text-center box-shadow text-bg-dark" id={this.props.id}>
// 				<div class="card-body">
// 					<h1 class="card-title text-light">{this.props.name}</h1>
// 					<p class="card-text">{this.props.desc}</p>
// 				</div>
// 			</div>
// 		</div>
// 	}
// }

// export default Card;

import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

export default function ActionAreaCard(name) {
  return (
    <Card sx={{ maxWidth: 345 }}>
      <CardActionArea>
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
            `$name`
          </Typography>
          <Typography variant="body2" color="text.secondary">
            Lizards are a widespread group of squamate reptiles, with over 6,000
            species, ranging across all continents except Antarctica
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
  );
}
