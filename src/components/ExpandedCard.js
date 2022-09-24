import React, { Component, useState } from 'react';

class ExpandedCard extends React.Component {
	render() {
		return <div>
			<div class="card text-center vw-25 h-50 box-shadow text-bg-dark" id={this.props.id}>
				<div class="card-body">
					<h1 class="card-title text-light">{this.props.header}</h1>
					<p class="card-text">{this.props.desc}</p>
				</div>
			</div>
		</div>
	}
}

export default ExpandedCard;