<?php
    session_save_path("./sessions/");
    session_start();
    include_once('flag.php');
?>
<html>
<head>
    <title>Bestiary</title>
</head>
<body style="background-color:#3CB371;">
<center><h1>Bestiary</h1></center>
<script>
function show()
{
    var monster = document.getElementById("monster").value;
    document.location.href = "index.php?monster="+monster;
}
</script>

<p>
<?php
    $monster = NULL;

    if(isset($_SESSION['monster']) && !empty($_SESSION['monster']))
        $monster = $_SESSION['monster'];
    if(isset($_GET['monster']) && !empty($_GET['monster']))
    {
        $monster = $_GET['monster'];
        $_SESSION['monster'] = $monster;
    }

    if($monster !== NULL && strpos($monster, "flag") === False)
        include($monster);
    else
        echo "Select a monster to read his description.";
?>
</p>

<select id="monster">
    <option value="beholder">Beholder</option>
    <option value="displacer_beast">Displacer Beast</option>
    <option value="mimic">Mimic</option>
    <option value="rust_monster">Rust Monster</option>
    <option value="gelatinous_cube">Gelatinous Cube</option>
    <option value="owlbear">Owlbear</option>
    <option value="lich">Lich</option>
    <option value="the_drow">The Drow</option>
    <option value="mind_flayer">Mind Flayer</option>
    <option value="tarrasque">Tarrasque</option>
</select> <input type="button" value="show description" onclick="show()">
<div style="font-size:70%">Source : https://io9.gizmodo.com/the-10-most-memorable-dungeons-dragons-monsters-1326074030</div><br />
</body>
</html>
