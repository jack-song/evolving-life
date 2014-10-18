var TILESIZE = 40,
	MAPSIZE = 50,
	DEFAULT_FONT = "bold " + TILESIZE*1.5 + "px monospace sans-serif";

var setup = function (lifeloop, toCSSColor){
	//get the geography points passed to page in context from django
	var canvas = $('#gamescreen')[0],
		context = canvas.getContext('2d');

	//set up canvas defaults
	canvas.width = TILESIZE * MAPSIZE;
	canvas.height = TILESIZE * MAPSIZE;
	context.font = DEFAULT_FONT;

	//draw the geography background first
	GEOGRAPHYPOINTS.forEach(function(geographypoint){
		context.fillStyle = toCSSColor(geographypoint.fields.geography[0]);
		context.fillText(geographypoint.fields.geography[1], geographypoint.fields.x * TILESIZE, geographypoint.fields.y * TILESIZE);
	});
}

var lifeloop = function (){

}

var toCSSColor = function(num) {
	if (num < 0)
    {
    	num = 0xFFFFFFFF + num + 1;
    }

    return "#" + Number(num).toString(16);
}

$(document).ready(setup(lifeloop, toCSSColor));