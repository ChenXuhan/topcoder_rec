# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ChallengeItem(models.Model):
    challengeid = models.IntegerField(db_column='challengeId', primary_key=True)  # Field name made lowercase.
    challengename = models.CharField(db_column='challengeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    challengetype = models.CharField(db_column='challengeType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectId', blank=True, null=True)  # Field name made lowercase.
    forumid = models.IntegerField(db_column='forumId', blank=True, null=True)  # Field name made lowercase.
    detailedrequirements = models.TextField(db_column='detailedRequirements', blank=True, null=True)  # Field name made lowercase.
    screeningscorecardid = models.IntegerField(db_column='screeningScorecardId', blank=True, null=True)  # Field name made lowercase.
    reviewscorecardid = models.IntegerField(db_column='reviewScorecardId', blank=True, null=True)  # Field name made lowercase.
    numberofcheckpointsprizes = models.IntegerField(db_column='numberOfCheckpointsPrizes', blank=True, null=True)  # Field name made lowercase.
    topcheckpointprize = models.CharField(db_column='topCheckPointPrize', max_length=255, blank=True, null=True)  # Field name made lowercase.
    currentstatus = models.CharField(db_column='currentStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    postingdate = models.CharField(db_column='postingDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationenddate = models.CharField(db_column='registrationEndDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submissionenddate = models.CharField(db_column='submissionEndDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    finalfixenddate = models.CharField(db_column='finalFixEndDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    appealsenddate = models.CharField(db_column='appealsEndDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    checkpointsubmissionenddate = models.CharField(db_column='checkpointSubmissionEndDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    forumlink = models.CharField(db_column='forumLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    registrationstartdate = models.CharField(db_column='registrationStartDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    digitalrunpoints = models.CharField(db_column='digitalRunPoints', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reliabilitybonus = models.FloatField(db_column='reliabilityBonus', blank=True, null=True)  # Field name made lowercase.
    technology = models.CharField(max_length=2000, blank=True, null=True)
    prize = models.CharField(max_length=255, blank=True, null=True)
    platforms = models.CharField(max_length=255, blank=True, null=True)
    numsubmissions = models.IntegerField(db_column='numSubmissions', blank=True, null=True)  # Field name made lowercase.
    numregistrants = models.IntegerField(db_column='numRegistrants', blank=True, null=True)  # Field name made lowercase.
    languages = models.CharField(max_length=1000, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    difficultydegree = models.FloatField(db_column='difficultyDegree', blank=True, null=True)  # Field name made lowercase.
    diff = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenge_item'


class ChallengePhase(models.Model):
    challengeid = models.IntegerField(db_column='challengeID', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    scheduledstarttime = models.CharField(db_column='scheduledStartTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actualstarttime = models.CharField(db_column='actualStartTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scheduledendtime = models.CharField(db_column='scheduledEndTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actualendtime = models.CharField(db_column='actualendTime', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'challenge_phase'


class ChallengeRegistrant(models.Model):
    challengeid = models.IntegerField(db_column='challengeID', blank=True, null=True)  # Field name made lowercase.
    handle = models.CharField(max_length=255, blank=True, null=True)
    reliability = models.CharField(max_length=255, blank=True, null=True)
    registrationdate = models.CharField(db_column='registrationDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.CharField(db_column='submissionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'challenge_registrant'


class ChallengeSubmissionDesign(models.Model):
    challengeid = models.IntegerField(db_column='challengeID', blank=True, null=True)  # Field name made lowercase.
    handle = models.CharField(max_length=255, blank=True, null=True)
    placement = models.CharField(max_length=255, blank=True, null=True)
    submissiondate = models.CharField(db_column='submissionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submissionstatus = models.CharField(db_column='submissionStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    points = models.CharField(max_length=255, blank=True, null=True)
    finalscore = models.FloatField(db_column='finalScore', blank=True, null=True)  # Field name made lowercase.
    screeningscore = models.CharField(db_column='screeningScore', max_length=255, blank=True, null=True)  # Field name made lowercase.
    initialscore = models.CharField(db_column='initialScore', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submissiondownloadlink = models.CharField(db_column='submissionDownloadLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'challenge_submission_design'


class ChallengeSubmissionDevelop(models.Model):
    challengeid = models.IntegerField(db_column='challengeID', blank=True, null=True)  # Field name made lowercase.
    handle = models.CharField(max_length=255, blank=True, null=True)
    placement = models.CharField(max_length=255, blank=True, null=True)
    submissiondate = models.CharField(db_column='submissionDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submissionstatus = models.CharField(db_column='submissionStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    points = models.CharField(max_length=255, blank=True, null=True)
    finalscore = models.FloatField(db_column='finalScore', blank=True, null=True)  # Field name made lowercase.
    screeningscore = models.CharField(db_column='screeningScore', max_length=255, blank=True, null=True)  # Field name made lowercase.
    initialscore = models.CharField(db_column='initialScore', max_length=255, blank=True, null=True)  # Field name made lowercase.
    submissiondownloadlink = models.CharField(db_column='submissionDownloadLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'challenge_submission_develop'


class Development(models.Model):
    handle = models.CharField(max_length=50, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    developtype = models.CharField(db_column='developType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activepercentile = models.CharField(db_column='activePercentile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reliability = models.CharField(max_length=100, blank=True, null=True)
    activerank = models.IntegerField(db_column='activeRank', blank=True, null=True)  # Field name made lowercase.
    activecountryrank = models.IntegerField(db_column='activeCountryRank', blank=True, null=True)  # Field name made lowercase.
    activeschoolrank = models.IntegerField(db_column='activeSchoolRank', blank=True, null=True)  # Field name made lowercase.
    overallpercentile = models.CharField(db_column='overallPercentile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    overallrank = models.IntegerField(db_column='overallRank', blank=True, null=True)  # Field name made lowercase.
    overallcountryrank = models.IntegerField(db_column='overallCountryRank', blank=True, null=True)  # Field name made lowercase.
    overallschoolrank = models.IntegerField(db_column='overallSchoolRank', blank=True, null=True)  # Field name made lowercase.
    volatility = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'development'


class DevelopmentHistory(models.Model):
    handle = models.CharField(max_length=100, blank=True, null=True)
    developtype = models.CharField(db_column='developType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    competitions = models.IntegerField(blank=True, null=True)
    submissions = models.IntegerField(blank=True, null=True)
    submissionrate = models.CharField(db_column='submissionRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inquiries = models.IntegerField(blank=True, null=True)
    passedscreening = models.IntegerField(db_column='passedScreening', blank=True, null=True)  # Field name made lowercase.
    screeningsuccessrate = models.CharField(db_column='screeningSuccessRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    passedreview = models.IntegerField(db_column='passedReview', blank=True, null=True)  # Field name made lowercase.
    reviewsuccessrate = models.CharField(db_column='reviewSuccessRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    appeals = models.IntegerField(blank=True, null=True)
    appealsuccessrate = models.CharField(db_column='appealSuccessRate', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField(blank=True, null=True)
    winpercentage = models.CharField(db_column='winPercentage', max_length=100, blank=True, null=True)  # Field name made lowercase.
    maximumscore = models.FloatField(db_column='maximumScore', blank=True, null=True)  # Field name made lowercase.
    minimumscore = models.FloatField(db_column='minimumScore', blank=True, null=True)  # Field name made lowercase.
    averagescore = models.FloatField(db_column='averageScore', blank=True, null=True)  # Field name made lowercase.
    averageplacement = models.FloatField(db_column='averagePlacement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'development_history'


class MyDesignDev(models.Model):
    challengeid = models.IntegerField(db_column='challengeId', primary_key=True)  # Field name made lowercase.
    challengename = models.CharField(db_column='challengeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectId', blank=True, null=True)  # Field name made lowercase.
    forumid = models.IntegerField(db_column='forumId', blank=True, null=True)  # Field name made lowercase.
    forumlink = models.CharField(db_column='forumLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(blank=True, null=True)
    difficultydegree = models.FloatField(db_column='difficultyDegree', blank=True, null=True)  # Field name made lowercase.
    technum = models.IntegerField(db_column='techNum', blank=True, null=True)  # Field name made lowercase.
    isjava = models.IntegerField(db_column='isJava', blank=True, null=True)  # Field name made lowercase.
    iscs = models.IntegerField(db_column='isCs', blank=True, null=True)  # Field name made lowercase.
    isjs = models.IntegerField(db_column='isJs', blank=True, null=True)  # Field name made lowercase.
    ishtml = models.IntegerField(db_column='isHTML', blank=True, null=True)  # Field name made lowercase.
    design_handle = models.CharField(max_length=255, blank=True, null=True)
    design_final_points = models.FloatField(blank=True, null=True)
    design_challengeid = models.IntegerField(db_column='design_challengeId', blank=True, null=True)  # Field name made lowercase.
    design_submission = models.IntegerField(blank=True, null=True)
    design_register = models.IntegerField(blank=True, null=True)
    umlsize = models.FloatField(db_column='umlSize', blank=True, null=True)  # Field name made lowercase.
    diagramnum = models.IntegerField(db_column='diagramNum', blank=True, null=True)  # Field name made lowercase.
    compages = models.IntegerField(db_column='comPages', blank=True, null=True)  # Field name made lowercase.
    reqpages = models.IntegerField(db_column='reqPages', blank=True, null=True)  # Field name made lowercase.
    dev_prize = models.IntegerField(blank=True, null=True)
    design_prize = models.IntegerField(blank=True, null=True)
    dev_duration = models.IntegerField(blank=True, null=True)
    design_duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_design_dev'


class RatingHistory(models.Model):
    developtype = models.CharField(db_column='developType', max_length=100, blank=True, null=True)  # Field name made lowercase.
    handle = models.CharField(max_length=100, blank=True, null=True)
    challengeid = models.IntegerField(db_column='challengeId', blank=True, null=True)  # Field name made lowercase.
    challengename = models.CharField(db_column='challengeName', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    date = models.CharField(max_length=100, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_history'


class User(models.Model):
    handle = models.CharField(unique=True, max_length=255)
    country = models.CharField(max_length=100, blank=True, null=True)
    membersince = models.CharField(db_column='memberSince', max_length=100, blank=True, null=True)  # Field name made lowercase.
    quote = models.TextField(blank=True, null=True)
    photolink = models.CharField(db_column='photoLink', max_length=100, blank=True, null=True)  # Field name made lowercase.
    copilot = models.IntegerField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    competitionnums = models.IntegerField(db_column='competitionNums', blank=True, null=True)  # Field name made lowercase.
    submissionnums = models.IntegerField(db_column='submissionNums', blank=True, null=True)  # Field name made lowercase.
    winnums = models.IntegerField(db_column='winNums', blank=True, null=True)  # Field name made lowercase.
    skilldegree = models.TextField(db_column='skillDegree', blank=True, null=True)  # Field name made lowercase.
    ability = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
