import './App.css';
import { useState } from 'react';
import useLocationStore from './store/locationStore';
import useScenarioStore from './store/scenarioStore';
import usePlanStore from './store/planStore';
import { Box, Button, Card, CardActionArea, CardContent, Chip, Container, Grid, Typography } from '@mui/material';

function App() {
  const locations = useLocationStore(state => state.locations);
  const scenarios = useScenarioStore(state => state.scenarios);
  const getLocations = useLocationStore(state => state.getLocations);
  const plans = usePlanStore(state => state.plans);
  const [selected, setSelected] = useState();
  const [stage, setStage] = useState("splash");
  const [year, setYear] = useState(1);

  const handleSelect = e => {
    setSelected(e.currentTarget.id);
  }
  const handleStage = e => {

    if (stage === "splash") {
      setStage("gamemode");
    }
    else if (stage === "gamemode") {
      setStage("location");
      setSelected(undefined);
      getLocations();
    }
    else if (stage === "location") {
      setStage("plan");
      setSelected(undefined);
    } else if (stage === "plan") {
      setStage("outcome");
      setSelected(undefined);
    } else if (year !== 10) {
      setStage("outcome");
      setYear(year + 1);
    } else {
      setStage("end");
    }
  }
  const startOver = e => {
    setStage("gamemode");
  }


  if (stage === "splash") {
    return (
      // <Stack spacing={2}>
      //   <Typography gutterBottom variant="h4" component="div" color="common.white" drop-shadow="1px">Item 1</Typography>
      //   {/* <Item>Item 2</Item>
      //   <Item>Item 3</Item> */}
      // </Stack>
      <Button variant="contained" onClick={() => handleStage()} size="large">Next</Button>
    );
  }
  else if (stage === "gamemode") {
    return (
      <Container maxWidth="xl" className="background">
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="75vh"
        >
          <Grid
            container
            spacing={2}
            alignItems="center"
            justifyContent="center"
          >
            <Grid
              item xs={3}
              style={{ display: 'flex' }}
              alignItems="center"
              justifyContent="center"
            >
              <Card
                id="home"
                sx={{ maxWidth: 345 }}
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  flexDirection: 'column',
                  backgroundColor: '#1976D2',
                }}
                onClick={(e) => handleSelect(e)}
              >
                <CardActionArea>
                  <CardContent>
                    <Typography gutterBottom variant="h4" component="div" color="common.white">
                      Home Insurance
                    </Typography>
                  </CardContent>
                </CardActionArea>
              </Card>
            </Grid>
            <Grid
              item xs={3}
              style={{ display: 'flex' }}
              alignItems="center"
              justifyContent="center"
            >
              <Card
                id="home"
                sx={{ maxWidth: 345 }}
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  flexDirection: 'column',
                  backgroundColor: '#1976D2',
                }}
                onClick={(e) => handleSelect(e)}
              >
                <CardActionArea>
                  <CardContent>
                    <Typography gutterBottom variant="h4" component="div" color="common.white">
                      Car Insurance
                    </Typography>
                  </CardContent>
                </CardActionArea>
              </Card>
            </Grid>
          </Grid>
        </Box>
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="0vh"
          maxHeight="75vh"
        >
          <Button disabled={selected === undefined} variant="contained" onClick={() => handleStage()} size="large">Next</Button>
        </Box>

      </Container>
    );
  }
  else if (stage === "location") {
    return (
      <Container maxWidth="xl" className="background">
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="75vh"
        >
          <Grid
            container
            spacing={2}
            alignItems="stretch"
          >
            {locations.map(item => (
              <Grid
                item xs={3}
                style={{ display: 'flex' }}
              >
                <Card
                  id={item.id}
                  sx={{ maxWidth: 345 }}
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    flexDirection: 'column',
                    backgroundColor: '#212529',
                  }}
                  onClick={(e) => handleSelect(e)}
                >
                  <CardActionArea>
                    <CardContent>
                      <Typography gutterBottom variant="h4" component="div" color="common.white">
                        {item.name}
                      </Typography>
                      <Typography variant="body1" color="#ADADAD">
                        {item.desc}
                      </Typography>
                    </CardContent>
                  </CardActionArea>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Box>
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="0vh"
          maxHeight="75vh"
        >
          <Button disabled={selected === undefined} variant="contained" onClick={() => handleStage()} size="large">Next</Button>
        </Box>

      </Container>
    );
  }
  else if (stage === "plan") {
    return (
      <Container maxWidth="xl" className="background">
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="75vh"
        >
          <Grid
            container
            spacing={2}
            alignItems="stretch"
          >
            {plans.map(item => (
              <Grid
                item xs={3}
                style={{ display: 'flex' }}
              >
                <Card
                  id={item.id}
                  sx={{ maxWidth: 345 }}
                  style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    flexDirection: 'column',
                    backgroundColor: '#212529',
                  }}
                  onClick={(e) => handleSelect(e)}
                >
                  <CardActionArea>
                    <CardContent>
                      <Typography gutterBottom variant="h4" component="div" color="common.white">
                        {item.header}
                      </Typography>
                      <Typography variant="body1" color="#ADADAD">
                        {item.desc}
                      </Typography>
                    </CardContent>
                  </CardActionArea>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Box>
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="0vh"
          maxHeight="75vh"
        >
          <Button disabled={selected === undefined} variant="contained" onClick={() => handleStage()} size="large">Next</Button>
        </Box>
      </Container>
    );
  }
  else if (stage === "outcome") {
    return (
      <Container maxWidth="xl" className="background">
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="75vh"
        >

          <Card
            sx={{ maxWidth: 1200 }}
            style={{
              display: 'flex',
              justifyContent: 'space-between',
              flexDirection: 'column',
              backgroundColor: '#212529',
            }}
          >
            <CardContent>
              <Typography gutterBottom variant="h2" component="div" color="common.white" display="flex" justifyContent="center">
                {scenarios[0].header}
              </Typography>
              <Typography variant="h5" color="#ADADAD">
                {scenarios[0].desc} {scenarios[0].result}
              </Typography>
            </CardContent>
          </Card>
        </Box>
        <Box
          maxWidth="xl"
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="0vh"
          maxHeight="75vh"
        >
          <Button variant="contained" onClick={() => handleStage()} size="large">Next</Button>
          <Chip label=<div>Year {year}</div> size="small" color="primary" />
        </Box>
      </Container >
    );
  }
  else if (stage === "end") {
    return (
      <Button variant="contained" onClick={() => startOver()} size="large">Start Over</Button>
      // <Container maxWidth="xl" className="background">
      //   <Box
      //     maxWidth="xl"
      //     display="flex"
      //     justifyContent="center"
      //     alignItems="center"
      //     minHeight="75vh"
      //   >
      //     <Card
      //       sx={{ maxWidth: 1200 }}
      //       style={{
      //         display: 'flex',
      //         justifyContent: 'space-between',
      //         flexDirection: 'column',
      //         backgroundColor: '#212529',
      //       }}
      //     >
      //       <CardContent>
      //         <Typography gutterBottom variant="h2" component="div" color="common.white" display="flex" justifyContent="center">
      //           congrats u reach the end
      //         </Typography>
      //       </CardContent>
      //     </Card>
      //   </Box>
      //   <Box
      //     maxWidth="xl"
      //     display="flex"
      //     justifyContent="center"
      //     alignItems="center"
      //     minHeight="0vh"
      //     maxHeight="75vh"
      //   >
      //     <Button variant="contained" onClick={() => handleStage()} size="large" color="green">Start Over</Button>
      //   </Box>
      // </Container >
    );
  }
}
export default App;
